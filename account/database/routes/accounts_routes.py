import datetime
from typing import Any, Coroutine, Union

from fastapi import APIRouter, Header, HTTPException
from fastapi.openapi.models import Response
from sqlalchemy.ext.asyncio import async_sessionmaker

from account.database.models.account_model import AccountResponse
from account.database.service.account_service import AccountService
from databases_config.postgres_base.postgres_engine import engine

router = APIRouter(
    prefix="/account",
    tags=["accounts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/accounts/{login}", response_model=AccountResponse)
async def get_account(
        login: str,
        x_api_key: str | None = Header(default=None)
) -> Coroutine[Any, Any, None]:
    if x_api_key != "qwerty":
        raise HTTPException(status_code=401, detail=f"Wrong api key")
    # Скоро уберу это убожество, да простят читающие
    account = await AccountService(async_sessionmaker(engine)).get_account_by_login(login)
    # .
    if account is None:
        raise HTTPException(status_code=404, detail=f"Account not found")
    return account


@router.post("accounts/{data}")
async def add_account(
        login: str,
        password: str,
        phone_number: str,
        mail: str,
        fullname: str,
        date_of_birth: datetime.date
) -> None:
    account_data = {"login": login,
                    "password": password,
                    "phone_number": phone_number,
                    "mail": mail,
                    "fullname": fullname,
                    "date_of_birth": date_of_birth}
    account = await AccountService(async_sessionmaker(engine)).add_new_account(account_data)


@router.put("accounts/{data}")
async def update_account(login: str,
                         mail: str,
                         password: str,
                         phone_number: str,
                         fullname: str,
                         date_of_birth: datetime.date) -> None:
    updated_data = {
        "login": login,
        "password": password,
        "phone_number": phone_number,
        "fullname": fullname,
        "date_of_birth": date_of_birth
    }
    account = await AccountService(async_sessionmaker(engine)).update_account_by_email(mail, **updated_data)

    # async def main():
    #     user_id = 1
    #     updated_data = {
    #         'fullname': 'John Doe',
    #         'phone_number': '1234567890',
    #         'mail': 'john.doe@example.com',
    #     }
    #
    #     await update_user(user_id, **updated_data)
    #     print('User updated successfully')
