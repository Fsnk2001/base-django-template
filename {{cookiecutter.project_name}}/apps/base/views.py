from abc import ABC

from rest_framework.viewsets import GenericViewSet

from .services import BaseService
from .pagination import CustomPagination


class BaseViewSet(ABC, GenericViewSet):
    _service: BaseService = None
    pagination_class = CustomPagination

    @classmethod
    def get_service(cls) -> BaseService:
        return cls._service

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)

        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', self.pagination_class.page_size))

        self.get_service().set_query_params(page, page_size)

        return request
