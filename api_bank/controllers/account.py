from app.repositories.account import create_account, list_accounts

async def create_new_account(session, account_data):
    return await create_account(session, account_data.owner, account_data.balance)

async def get_all_accounts(session):
    return await list_accounts(session)