from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from ..base.views import BaseViewSet
from ..base.responses import Response
from ..base.permissions import IsAdminPermission
from .serializers import (
    UserSerializer,
    CreateUserSerializer,
    UpdateUserSerializer,
    ResetPasswordSerializer,
)
from .services import UserService


class UserViewSet(BaseViewSet):
    _service = UserService
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get list of users",
        description="This endpoint gets all users.",
        responses=UserSerializer,
    )
    def list(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminPermission]
        self.check_permissions(request)

        users = self._service.get_all()
        return Response(
            data={
                "users": self.get_serializer(users, many=True).data
            }, message="List of users.", meta={}
        )

    @extend_schema(
        summary="Get a user",
        description="This endpoint gets a user.",
        responses=UserSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminPermission]
        self.check_permissions(request)

        id = kwargs.get('pk')
        user = self._service.get_by_id(id)
        return Response(
            data={
                "user": self.get_serializer(user).data
            }, message="The user.", meta={}
        )

    @extend_schema(
        summary="Get you",
        description="This endpoint gets you.",
        responses=UserSerializer,
    )
    @action(detail=False, methods=['get'], url_path='me')
    def get_me(self, request, *args, **kwargs):
        user_id = request.user.id
        user = self._service.get_by_id(user_id)
        return Response(
            data={
                "user": self.get_serializer(user).data
            }, message="The user.", meta={}
        )

    @extend_schema(
        request=CreateUserSerializer,
        summary="Create a user",
        description="This endpoint creates a user.",
        responses=UserSerializer,
    )
    def create(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminPermission]
        self.check_permissions(request)

        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self._service.create(serializer.validated_data)
        return Response(
            data={
                "user": self.get_serializer(user).data
            }, message="User created successfully.", status=status.HTTP_201_CREATED
        )

    @extend_schema(
        request=UpdateUserSerializer,
        summary="Update a user",
        description="This endpoint updates a user.",
        responses=UserSerializer,
    )
    def update(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminPermission]
        self.check_permissions(request)

        id = kwargs.get('pk')
        serializer = UpdateUserSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_user = self._service.update(id, serializer.validated_data)
        return Response(
            data={
                "user": self.get_serializer(updated_user).data
            }, message="User updated successfully.", status=status.HTTP_200_OK
        )

    @extend_schema(
        request=ResetPasswordSerializer,
        summary="Reset user's password",
        description="This endpoint resets a user's password.",
        responses=UserSerializer,
    )
    @action(detail=False, methods=['post'], url_path='reset-password')
    def reset_password(self, request, *args, **kwargs):
        user_id = request.user.id
        serializer = ResetPasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        user = self._service.reset_password(user_id, serializer.validated_data.get('password'))
        return Response(
            data={
                "user": self.get_serializer(user).data
            }, message="User's password updated successfully.", meta={}
        )

    @extend_schema(
        summary="Delete a user",
        description="This endpoint deletes a user.",
    )
    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminPermission]
        self.check_permissions(request)

        id = kwargs.get('pk')
        self._service.delete(id)
        return Response(
            data={}, message="User deleted successfully.", status=status.HTTP_200_OK
        )
