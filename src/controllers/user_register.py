from src.models.repositories.interfaces.users_repository_interface import UsersRepositoryInterface


class UserRegister:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository
