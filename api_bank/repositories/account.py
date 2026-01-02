from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.account import Account

async def create_account(session: AsyncSession, owner: str, balance: float):
    acc = Account(owner=owner, balance=balance)
    session.add(acc)
    await session.commit()
    await session.refresh(acc)
    return acc

async def list_accounts(session: AsyncSession):
    result = await session.execute(select(Account))
    return result.scalars().all()