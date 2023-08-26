from datetime import datetime, date

from pydantic import BaseModel


class AccountResponse(BaseModel):
    account_id: int
    create_date: datetime
    login: str
    password: str
    phone_number: str
    mail: str
    fullname: str
    date_of_birth: date
