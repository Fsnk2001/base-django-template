from django.urls import path, include
from rest_framework.routers import DefaultRouter
{%- if cookiecutter.use_jwt == 'y' %}
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
{%- endif %}

from .views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')
urlpatterns = [
{%- if cookiecutter.use_jwt == 'y' %}
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
{%- endif %}
    path('', include(router.urls)),
]
