# pylint:disable = W0212
from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler

class UsersRepositoryInterface(ABC):
    @abstractmethod
    async def insert_users(self, user_infos: dict) -> None:
        pass

    @abstractmethod
    async def get_users_by_name(self, user_name: str) -> list[dict]:
        pass