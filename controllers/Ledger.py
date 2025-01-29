from enum import Enum
from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from Enums.base_enum import combined_enums, BaseLedgerOperation, LedgerOperation
from constants.constants import LEDGER_OPERATION_CONFIG
from models.User import User, LedgerEntry
from sqlalchemy.orm import Session
from models.schematics.schemas import LedgerEntryCreate

CombinedLedgerOperation = combined_enums(BaseLedgerOperation, LedgerOperation)


def get_ledger_balacnce(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Owner not found")

    current_balance = db.query(func.sum(LedgerEntry.amount)).filter(
        LedgerEntry.owner_id == user_id,
    ).scalar() or 0

    return {"owner_id": user_id, "current_balance": current_balance}


def create_ledger_entry(entry: LedgerEntryCreate, db: Session):
    try:
        operation_enum = CombinedLedgerOperation[entry.operation].value.value
        print(operation_enum)
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid operation")

    user = db.query(User).filter(User.id == entry.owner_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Owner not found")

    if db.query(LedgerEntry).filter(LedgerEntry.nonce == entry.nonce).first():
        raise HTTPException(status_code=400, detail="Duplicate transaction detected")

    if operation_enum in {CombinedLedgerOperation}:

        current_balance = db.query(func.sum(LedgerEntry.amount)).filter(
            LedgerEntry.owner_id == entry.owner_id
        ).scalar() or 0

        if current_balance < entry.amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")

    new_entry = LedgerEntry(
        owner_id=entry.owner_id,
        operation=operation_enum,
        amount=LEDGER_OPERATION_CONFIG[entry.operation],
        nonce=entry.nonce
    )
    db.add(new_entry)

    try:
        db.commit()
        return {"message": "Ledger entry created successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create ledger entry")
