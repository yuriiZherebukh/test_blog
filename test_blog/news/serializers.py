"""
Module contains serializer for News model
"""

from rest_framework import serializers

from authentication.serializers import CustomUserSerializer
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    """
    Serializes News model
    """

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = News
        fields = ('id', 'author', 'title', 'text', 'created_date')
