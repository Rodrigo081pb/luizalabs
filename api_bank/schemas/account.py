from pydantic import BaseModel

class AccountCreate(BaseModel):
    owner: str
    balance: float = 0.0

class AccountOut(AccountCreate):
    id: int

    class Config:
        orm_mode = True