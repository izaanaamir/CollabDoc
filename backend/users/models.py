from django.contrib.auth.models import AbstractBaseUser  # noqa
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        if not email:
            raise ValueError("The Email field cannot be empty")
        if not password:
            raise ValueError("The Password field cannot be empty ")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=20, unique=True, null=True, blank=True
    )
    password_hash = models.CharField(max_length=255)
    timezone = models.CharField(max_length=50, default="UTC")
    avatar = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "password"]

    def __str__(self):
        return self.email
