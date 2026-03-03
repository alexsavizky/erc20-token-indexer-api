from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Wallet, TransferEvent

router = APIRouter()


# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/wallet/{address}")
def get_wallet_balance(address: str, db: Session = Depends(get_db)):
    # Query the wallet by address (case-insensitive check is safer)
    wallet = db.query(Wallet).filter(Wallet.address.ilike(address)).first()

    if not wallet:
        return {"address": address, "balance": 0, "message": "Wallet not yet indexed"}

    return {
        "address": wallet.address,
        "balance": str(wallet.balance),  # Convert Decimal to string for JSON
    }


@router.get("/transfers/{address}")
def get_wallet_history(address: str, db: Session = Depends(get_db)):
    # Find transfers where the address is either the sender OR receiver
    transfers = (
        db.query(TransferEvent)
        .filter(
            (TransferEvent.from_address.ilike(address))
            | (TransferEvent.to_address.ilike(address))
        )
        .all()
    )

    return {"address": address, "total_transfers": len(transfers), "history": transfers}
