from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from db.database import get_db
from models.schematics.schemas import LedgerEntryCreate
from sqlalchemy.orm import Session
from controllers.Ledger import get_ledger_balacnce

router = APIRouter(
    prefix="/ledger",
    tags=["users"],
)


@router.get("/{owner_id}")
async def get_current_balance(owner_id: int, db: Session = Depends(get_db)):
    user_balance = get_ledger_balacnce(owner_id, db)
    if user_balance is None:
        raise HTTPException(status_code=404, detail="Owner not found")

    return user_balance


@router.post("/")
async def create_ledger_entry(entry: LedgerEntryCreate, db: Session = Depends(get_db)):
    from controllers.Ledger import create_ledger_entry

    try:
        return create_ledger_entry(entry, db)
    except HTTPException as e:
        raise e
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create ledger entry")
