from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    country = models.CharField(max_length=50, null=True)
    is_super_admin = models.BooleanField(default=False)
    is_quest = models.BooleanField(default=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
