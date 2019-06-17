from rest_framework import serializers

from news.models import News
from authentication.serializers import CustomUserSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = News
        fields = ('id', 'author', 'title', 'text')
