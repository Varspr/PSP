from pydantic.v1 import BaseSettings


class DatabaseConfig(BaseSettings):
    login: str = "postgres"
    password: str = "password"
    host: str = "localhost"
    port: str = "5432"
    database: str = "postgres"


config = DatabaseConfig()

