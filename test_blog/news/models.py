from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import CustomUser


class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @staticmethod
    def get_by_id(news_id):
        try:
            return News.objects.get(id=news_id)
        except ObjectDoesNotExist:
            return None
