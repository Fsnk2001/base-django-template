from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from ..base.models import BaseModel
from .managers import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username

    def is_staff(self):
        return self.is_admin


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return f'User ({self.user.username})\'s profile'
