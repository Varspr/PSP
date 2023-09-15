import asyncio

import uvicorn
from fastapi import FastAPI

from account.database.routes import accounts_routes

app = FastAPI()
app.include_router(accounts_routes.router)


# async def main():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
if __name__ == "__main__":
    # asyncio.run(main())
    uvicorn.run(app, host="127.0.0.1", port=8080)
