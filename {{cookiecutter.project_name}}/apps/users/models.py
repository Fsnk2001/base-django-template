from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group

from ..base.models import BaseModel
from .managers import UserManager
from .roles import UserRoles


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username

    def add_role(self, role_name):
        group, created = Group.objects.get_or_create(name=role_name)
        self.groups.add(group)

    def remove_role(self, role_name):
        group = Group.objects.filter(name=role_name).first()
        if group:
            self.groups.remove(group)

    def has_role(self, role_name):
        return self.groups.filter(name=role_name).exists()

    def get_roles(self):
        return [group.name for group in self.groups.all()]

    @property
    def is_admin(self):
        return self.has_role(UserRoles.ADMIN)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return f'User ({self.user.username})\'s profile'
