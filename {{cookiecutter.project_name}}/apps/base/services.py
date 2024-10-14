from abc import ABC
from typing import Type, TypeVar

from django.db.models import QuerySet

from .repositories import BaseRepository, ModelInstance

Repository = TypeVar('Repository', bound='BaseRepository')


class BaseService(ABC):
    _repository: BaseRepository = None

    @classmethod
    def get_repository(cls: Type[Repository]) -> Repository:
        return cls._repository

    @classmethod
    def set_filters(cls, params) -> None:
        cls.get_repository().set_filters(params)

    @classmethod
    def set_query_params(cls, page: int, page_size: int) -> None:
        cls.get_repository().set_query_params(page, page_size)

    @classmethod
    def get_all(cls) -> QuerySet:
        return cls.get_repository().get_all()

    @classmethod
    def get_all_with_pagination(cls) -> (QuerySet, dict):
        return cls.get_repository().get_all_with_pagination()

    @classmethod
    def get_by_id(cls, id: int | str) -> ModelInstance:
        return cls.get_repository().get_by_id(id)

    @classmethod
    def get_and_lock_for_update(cls, id: int | str) -> ModelInstance:
        return cls.get_repository().get_and_lock_for_update(id)

    @classmethod
    def create(cls, data: dict) -> ModelInstance:
        return cls.get_repository().create(data)

    @classmethod
    def update(cls, id: int | str, data: dict) -> ModelInstance:
        instance = cls.get_by_id(id)
        return cls.get_repository().update(instance, data)

    @classmethod
    def delete(cls, id: int | str) -> None:
        instance = cls.get_by_id(id)
        cls.get_repository().delete(instance)

    @classmethod
    def check_related_user_id(cls, id: int | str, user_id: int | str) -> None:
        cls.get_repository().check_related_user_id(id, user_id)
