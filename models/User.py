import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from Enums.base_enum import LedgerOperation, combined_enums, BaseLedgerOperation
from db.database import Base

CombinedLedgerOperation = combined_enums(BaseLedgerOperation, LedgerOperation)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    ledger_entries = relationship("LedgerEntry", back_populates="owner")


class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(Enum(CombinedLedgerOperation), nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)

    owner = relationship("User", back_populates="ledger_entries")
