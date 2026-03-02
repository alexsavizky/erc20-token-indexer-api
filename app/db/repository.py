from decimal import Decimal
from db.session import SessionLocal
from db.models import TransferEvent


def save_transfer_to_db(transfer_data: dict):
    """Takes a dictionary of data and commits it to Postgres."""
    db = SessionLocal()
    try:
        new_transfer = TransferEvent(
            tx_hash=transfer_data["tx_hash"],
            block_number=transfer_data["block_number"],
            from_address=transfer_data["from"],
            to_address=transfer_data["to"],
            amount=Decimal(transfer_data["value"]),
        )
        db.add(new_transfer)
        db.commit()
        print(f"✅ Successfully indexed: {transfer_data['tx_hash'][:10]}...")
    except Exception as e:
        db.rollback()
        print(f"❌ Database error: {e}")
    finally:
        db.close()
