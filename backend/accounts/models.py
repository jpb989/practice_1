from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, name, password, **kwargs):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        if kwargs.get("is_staff") is not True:
            ValueError("is_staff must be True for superuser")
        if kwargs.get("is_superuser") is not True:
            ValueError("is_superuser must be True for superuser")
        
        return self.create_user(email, name, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

