from abc import ABC, abstractmethod
from typing import Type

from django.db.models import QuerySet

from .models import BaseModel
from .serializers import BaseModelSerializer


class BaseRepository(ABC):

    def __init__(self):
        self._model: Type[BaseModel] = self._get_model()
        self._serializer: Type[BaseModelSerializer] = self._get_serializer()

    @abstractmethod
    def _get_model(self) -> Type[BaseModel]:
        pass

    @abstractmethod
    def _get_serializer(self) -> Type[BaseModelSerializer]:
        pass

    def get_queryset(self) -> QuerySet:
        return self._model.objects.get_queryset()

    def set_filters(self, filters):
        pass

    def get_all(self) -> BaseModel:
        return self._model.objects.get_queryset().all()

    def get_by_id(self, id: int | str) -> BaseModel:
        return self._model.objects.filter(pk=id).first()

    def create(self, data: dict) -> BaseModel:
        serializer = self._serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def update(self, instance: BaseModel, data: dict) -> BaseModel:
        serializer = self._serializer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def delete(self, instance: BaseModel) -> None:
        instance.soft_delete()
