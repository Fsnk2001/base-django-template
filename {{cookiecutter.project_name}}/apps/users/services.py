from ..base.repositories import BaseRepository
from ..base.services import BaseService
from .repositories import UserRepository


class UserService(BaseService):

    def _get_repository(self) -> BaseRepository:
        return UserRepository()
