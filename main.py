import asyncio

import uvicorn
from fastapi import FastAPI

from Accounts.databases.base.base import Base
from Accounts.databases.base.postgres_base import engine
from Accounts.databases.schemas.account_schema import UserAccount

from Accounts.databases.routes import accounts_routes

app = FastAPI()
app.include_router(accounts_routes.router)


# async def main():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
if __name__ == "__main__":
    # asyncio.run(main())
    uvicorn.run(app, host="127.0.0.1", port=8080)
