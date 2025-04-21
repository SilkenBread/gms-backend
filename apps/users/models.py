from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, id, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo es obligatorio.")
        if not id:
            raise ValueError("La cédula es obligatoria.")
        email = self.normalize_email(email)
        user = self.model(id=id, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, id, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(id, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, max_length=20, verbose_name="ID number")
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    USER_TYPE_CHOICES = [
        ("employee", "employee"),
        ("member", "member"),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["id", "name", "surname", "user_type"]

    objects = UserManager()

    def __str__(self):
        return self.email
