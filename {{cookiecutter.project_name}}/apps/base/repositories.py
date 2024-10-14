from abc import ABC
from typing import Type, TypeVar

from django.db.models import QuerySet

from .models import BaseModel
from .serializers import BaseModelSerializer
from .exceptions import NotFoundError, PermissionDeniedError

ModelInstance = TypeVar('ModelInstance', bound='BaseModel')


class BaseRepository(ABC):
    _model: Type[BaseModel] = None
    _serializer: Type[BaseModelSerializer] = None
    page = None
    page_size = None

    @classmethod
    def _get_model(cls) -> Type[BaseModel]:
        return cls._model

    @classmethod
    def get_serializer(cls, *args, **kwargs) -> BaseModelSerializer:
        return cls._serializer(*args, **kwargs)

    @classmethod
    def get_queryset(cls) -> QuerySet:
        return cls._get_model().objects.get_queryset()

    @classmethod
    def get_by_pagination(cls, queryset: QuerySet) -> (QuerySet, dict):
        count = queryset.count()
        total_page = (count + cls.page_size - 1) // cls.page_size
        return queryset[(cls.page - 1) * cls.page_size:cls.page * cls.page_size], {
            'page': cls.page,
            'count': count,
            'total_page': total_page
        }

    @classmethod
    def set_filters(cls, filters) -> None:
        pass

    @classmethod
    def set_query_params(cls, page: int, page_size: int) -> None:
        cls.page = page
        cls.page_size = page_size

    @classmethod
    def get_all(cls) -> QuerySet:
        return cls._get_model().objects.get_queryset().all()

    @classmethod
    def get_all_with_pagination(cls) -> (QuerySet, dict):
        queryset = cls._get_model().objects.get_queryset().all()
        return cls.get_by_pagination(queryset)

    @classmethod
    def get_by_id(cls, id: int | str) -> ModelInstance:
        instance = cls._get_model().objects.filter(pk=id).first()
        if instance is None:
            raise NotFoundError()
        return instance

    @classmethod
    def get_and_lock_for_update(cls, id: int | str) -> ModelInstance:
        instance = cls._get_model().objects.select_for_update().filter(pk=id).first()
        if instance is None:
            raise NotFoundError()
        return instance

    @classmethod
    def create(cls, data: dict) -> ModelInstance:
        serializer = cls.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @classmethod
    def update(cls, instance: BaseModel, data: dict) -> ModelInstance:
        serializer = cls.get_serializer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @classmethod
    def delete(cls, instance: BaseModel) -> None:
        instance.delete()

    @classmethod
    def check_related_user_id(cls, id: int | str, user_id: int | str) -> None:
        instance = cls.get_by_id(id)
        if instance.user_id != user_id:
            raise PermissionDeniedError()
