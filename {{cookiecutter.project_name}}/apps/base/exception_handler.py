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
            errors={
                "error": "Not Found"
            },
            message="Data not found",
            meta={},
            status=404
        )

    if isinstance(exc, ValidationError):
        return Response(
            errors=exc.detail,
            message="Validation error",
            meta={},
            status=exc.status_code
        )

    if isinstance(exc, CustomException):
        return Response(
            errors=exc.details,
            message=exc.message,
            status=exc.status_code
        )

    if isinstance(exc, NotAuthenticated):
        return Response(
            message=exc.detail,
            meta={},
            status=exc.status_code
        )

    if isinstance(exc, APIException):
        message = 'API error occurred.'
        try:
            message = exc.detail['detail']
        except:
            pass
        return Response(
            message=message,
            meta={},
            status=exc.status_code
        )

    if response is None:
        return Response(
            data=None,
            message="An unexpected error occurred. Please try again later or contact support if the issue persists.",
            status=500
        )

    return response
