from decimal import Decimal
from app.db.session import SessionLocal
from app.db.models import TransferEvent, Wallet


def save_transfer_to_db(transfer_data: dict):
    """Saves transfer and updates balances in one atomic transaction."""
    db = SessionLocal()
    try:
        # 1. Duplicate Check
        existing_tx = (
            db.query(TransferEvent).filter_by(tx_hash=transfer_data["tx_hash"]).first()
        )
        if existing_tx:
            print(f"⏩ Skipping: {transfer_data['tx_hash'][:10]}... (Already Indexed)")
            return

        # 2. Create Transfer Record
        new_transfer = TransferEvent(
            tx_hash=transfer_data["tx_hash"],
            block_number=transfer_data["block_number"],
            from_address=transfer_data["from"],
            to_address=transfer_data["to"],
            amount=Decimal(transfer_data["value"]),
        )
        db.add(new_transfer)

        # 3. Update Wallet Balances
        update_wallet_balances(
            db,
            transfer_data["from"],
            transfer_data["to"],
            transfer_data["value"],
        )

        # 4. Final Commit (This saves EVERYTHING at once)
        db.commit()
        print(f"✅ Indexed & Balanced: {transfer_data['tx_hash'][:10]}...")

    except Exception as e:
        db.rollback()  # If anything fails, nothing is saved
        print(f"❌ Database error: {e}")
    finally:
        db.close()


def update_wallet_balances(db, from_addr, to_addr, amount):
    """Updates balances for both parties within the existing session."""
    # Handle Sender (Subtract)
    sender = db.query(Wallet).filter_by(address=from_addr).first()
    if not sender:
        sender = Wallet(address=from_addr, balance=Decimal(0))
        db.add(sender)
    sender.balance -= Decimal(amount)

    # Handle Receiver (Add)
    receiver = db.query(Wallet).filter_by(address=to_addr).first()
    if not receiver:
        receiver = Wallet(address=to_addr, balance=Decimal(0))
        db.add(receiver)
    receiver.balance += Decimal(amount)
