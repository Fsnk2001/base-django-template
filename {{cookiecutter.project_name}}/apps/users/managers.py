from django.contrib.auth.models import BaseUserManager

from .roles import UserRoles


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set.")

        user = self.model(username=username, **extra_fields)
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username, password, **extra_fields)

        user.is_active = True
        user.is_superuser = True
        user.full_clean()
        user.save(using=self._db)

        user.add_role(UserRoles.ADMIN)

        return user
