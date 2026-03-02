from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class TransferEvent(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    tx_hash = Column(String, unique=True, index=True, nullable=False)
    block_number = Column(BigInteger, nullable=False)
    from_address = Column(String, index=True, nullable=False)
    to_address = Column(String, index=True, nullable=False)
    # Using Numeric for high precision (ERC-20 values can be huge)
    amount = Column(Numeric, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Wallet(Base):
    __tablename__ = "wallets"

    address = Column(String, primary_key=True, index=True)
    balance = Column(Numeric, default=0)
    last_updated_block = Column(BigInteger)
