from abc import ABC, abstractmethod

from .models import BaseModel
from .repositories import BaseRepository
from .exceptions import NotFoundError


class BaseService(ABC):

    def __init__(self):
        self._repository: BaseRepository = self._get_repository()

    @abstractmethod
    def _get_repository(self) -> BaseRepository:
        pass

    def set_filters(self, params):
        self._repository.set_filters(params)

    def get_all(self) -> BaseModel:
        return self._repository.get_all()

    def get_by_id(self, id: int | str) -> BaseModel:
        instance = self._repository.get_by_id(id)
        if instance is None:
            raise NotFoundError()
        return instance

    def create(self, data: dict) -> BaseModel:
        return self._repository.create(data)

    def update(self, id: int | str, data: dict) -> BaseModel:
        instance = self.get_by_id(id)
        return self._repository.update(instance, data)

    def delete(self, id: int | str) -> None:
        instance = self.get_by_id(id)
        self._repository.delete(instance)
