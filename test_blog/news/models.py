"""
This module contains News Model
"""

from typing import Union

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone

from authentication.models import CustomUser


class News(models.Model):
    """
    News Model to operate with News Entity
    """

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @staticmethod
    def get_by_id(news_id: int) -> Union['News', None]:
        """
        Get :class:`.News` by id

        :param news_id: News id
        :return: News object or None
        """

        try:
            return News.objects.get(id=news_id)
        except ObjectDoesNotExist:
            return None
