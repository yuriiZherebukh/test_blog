import logging

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email


class CustomUser(AbstractUser):
    """
    Class model with User account
    """

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    @staticmethod
    def create(username: str, password: str, email: str):
        """
        Create base user with valid data

        :param username: User's username
        :param password: User's password
        :param email: User's email

        :return: Custom user object
        :raises ValidationError: In case some field wasn't validated successfully
        """
        try:
            user = CustomUser()

            user.username = username

            validate_email(email)
            user.email = email
            validate_password(password)
            user.set_password(password)
            user.save()
            return user
        except ValidationError as err:
            logging.error(err)
            return

    @staticmethod
    def get_by_username(username):
        try:
            return CustomUser.objects.get(username=username)
        except ObjectDoesNotExist:
            return None
