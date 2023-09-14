
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from Accounts.database.schemas.account_schema import UserAccount


class AccountService:
    def __init__(self, async_session: async_sessionmaker[AsyncSession]):
        self.async_session = async_session

    async def add_new_account(self, user_data: dict) -> None:
        async with self.async_session() as session:
            user = UserAccount(**user_data)
            session.add(user)
            await session.commit()
            await session.close()

    async def add_account(self, login: str,
                          password: str,
                          phone_number: str,
                          mail: str,
                          fullname: str,
                          date_of_birth: str) -> None:
        async with self.async_session() as session:
            user = UserAccount(login=login,
                               password=password,
                               phone_number=phone_number,
                               mail=mail,
                               fullname=fullname,
                               date_of_birth=date_of_birth)
            session.add(user)
            await session.commit()
            await session.close()

    async def get_account_by_login(self, login: str) -> None:
        async with self.async_session() as session:
            search_account = select(UserAccount).filter(UserAccount.login == login)

            result = await session.execute(search_account)

            account = result.scalar()

            return account

    async def update_account_by_email(self, mail, **kwargs):
        async with self.async_session() as session:
            user = await session.execute(
                UserAccount.__table__.update()
                .where(UserAccount.mail == mail)
                .values(**kwargs)
            )
            await session.commit()

            await session.close()




