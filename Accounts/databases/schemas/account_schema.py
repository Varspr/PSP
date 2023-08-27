import datetime

from sqlalchemy import func, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from Accounts.databases.base.base import Base


class UserAccount(Base):
    __tablename__ = 'users_accounts'

    account_id: Mapped[int] = mapped_column(primary_key=True,
                                            autoincrement=True)
    create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    login: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(13), unique=True)
    mail: Mapped[str] = mapped_column(String(30), unique=True, nullable=True)
    fullname: Mapped[str] = mapped_column(String(50))
    id_card: Mapped[str] = mapped_column(String)
    date_of_birth: Mapped[datetime.date] = mapped_column(Date)

    def __repr__(self):
        return f"Пользователь - {self.fullname} с id - {self.account_id}, был создан - {self.create_date}, " \
               f"принимает рассылки на почту - {self.mail}, логин аккаунта - {self.login}. Остальные данные - " \
               f"номер телефона - {self.phone_number}, дата рождения - {self.date_of_birth}, пароль - {self.password}"

    def to_dict(self):
        return {"id": self.account_id,
                "create_date": self.create_date,
                "login": self.login,
                "password": self.password,
                "phone_number": self.phone_number,
                "mail": self.mail,
                "fullname": self.fullname,
                "date_of_birth": self.date_of_birth}

    def update_account(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
