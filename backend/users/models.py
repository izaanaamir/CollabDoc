from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone as tz


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


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=20, unique=True, null=True, blank=True
    )
    timezone = models.CharField(max_length=50, default="UTC")
    avatar = models.URLField(blank=True)
    created_at = models.DateTimeField(default=tz.now())
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.pk and self.is_active:
            self.last_login = tz.now()
        super().save(*args, **kwargs)
