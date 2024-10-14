from ..base.services import BaseService
from .repositories import UserRepository


class UserService(BaseService):
    _repository = UserRepository

    @classmethod
    def reset_password(cls, id, password):
        user = cls.get_by_id(id)
        return cls._repository.change_password(user, password)
