from abc import ABC, abstractmethod

from rest_framework.viewsets import GenericViewSet

from .services import BaseService


class BaseViewSet(ABC, GenericViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._service: BaseService = self._get_service()

    @abstractmethod
    def _get_service(self) -> BaseService:
        pass
