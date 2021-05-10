from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from .validators import only_letters_validator, phone_number_validator


class UserManager(BaseUserManager):
    def create_user(self, first_name, password, phone, email, last_name=None):
        """Creates and saves a User."""
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj


class User(AbstractBaseUser):
    """User model in db."""
    first_name = models.CharField(max_length=124)
    last_name = models.CharField(max_length=124, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=50, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['pk']
