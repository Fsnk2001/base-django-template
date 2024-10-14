from django.http import Http404
from rest_framework.exceptions import APIException, ValidationError, NotAuthenticated
from rest_framework.views import exception_handler

from {{cookiecutter.project_slug}}.settings.base import DEBUG
from .exceptions import CustomException
from .responses import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if DEBUG:
        raise exc

    if isinstance(exc, Http404):
        return Response(
            errors="Not found",
            message="Item not found.",
            status=404,
        )

    if isinstance(exc, ValidationError):
        return Response(
            errors=exc.detail,
            message="Validation error.",
            status=exc.status_code,
        )

    if isinstance(exc, NotAuthenticated):
        return Response(
            errors="Not authenticated.",
            message=exc.detail,
            status=exc.status_code,
        )

    if isinstance(exc, APIException):
        try:
            message = exc.detail['detail']
        except:
            message = "API error occurred."
        return Response(
            message=message,
            status=exc.status_code,
        )

    if isinstance(exc, CustomException):
        return Response(
            errors=exc.details,
            message=exc.message,
            status=exc.status_code,
        )

    if response is None:
        return Response(
            message="An unexpected error occurred. Please try again later or contact support if the issue persists.",
            status=500
        )

    return response
