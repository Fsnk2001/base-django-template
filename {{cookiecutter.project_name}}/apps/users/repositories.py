from typing import Type

from ..base.models import BaseModel
from ..base.serializers import BaseModelSerializer
from ..base.repositories import BaseRepository
from .models import User
from .serializers import UserSerializer


class UserRepository(BaseRepository):

    def _get_model(self) -> Type[BaseModel]:
        return User

    def _get_serializer(self) -> Type[BaseModelSerializer]:
        return UserSerializer
