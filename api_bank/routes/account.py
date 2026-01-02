from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.schemas.account import AccountCreate, AccountOut
from app.controllers.account import create_new_account, get_all_accounts
from typing import List

router = APIRouter()

@router.post("/accounts/", response_model=AccountOut)
async def create_account_route(account: AccountCreate, session: AsyncSession = Depends(get_async_session)):
    return await create_new_account(session, account)

@router.get("/accounts/", response_model=List[AccountOut])
async def list_accounts_route(session: AsyncSession = Depends(get_async_session)):
    return await get_all_accounts(session)