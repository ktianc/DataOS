from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from shortuuidfield import ShortUUIDField

class UserManger(BaseUserManager):
    def _create_user(self, username, password, **kwargs):
        if not username:
            return ValueError("username cannot be empty")
        elif not password:
            return ValueError("password cannot be empty")
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, **kwargs):
        kwargs["is_superuser"] = "False"
        return self._create_user(username=username, password=password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        kwargs["is_superuser"] = "True"
        return self._create_user(username=username, password=password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    email = models.EmailField(unique=True,null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"

    object = UserManger()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username




