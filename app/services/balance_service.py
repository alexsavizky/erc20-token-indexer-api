from decimal import Decimal
from db.models import Wallet


def update_wallet_balances(db, from_addr, to_addr, amount):
    # 1. Update Sender (from_addr)
    sender = db.query(Wallet).filter_by(address=from_addr).first()
    if not sender:
        sender = Wallet(address=from_addr, balance=0)
        db.add(sender)
    sender.balance -= Decimal(amount)

    # 2. Update Receiver (to_addr)
    receiver = db.query(Wallet).filter_by(address=to_addr).first()
    if not receiver:
        receiver = Wallet(address=to_addr, balance=0)
        db.add(receiver)
    receiver.balance += Decimal(amount)
