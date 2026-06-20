from abc import abstractmethod, ABC


class UserRegisterInterface(ABC):
    @abstractmethod
    async def register_user(self, user_data: dict) -> dict:
        pass