from dataclasses import Field

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class LedgerEntryCreate(BaseModel):
    owner_id: int
    operation: str
    amount: int
    nonce: str