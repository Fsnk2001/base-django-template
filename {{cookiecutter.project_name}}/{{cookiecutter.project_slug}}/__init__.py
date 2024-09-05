{% if cookiecutter.use_celery == 'y' -%}
from .celery import app as celery_app

__all__ = ("celery_app",)
{% endif -%}
