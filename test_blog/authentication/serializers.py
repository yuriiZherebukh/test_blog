"""
This module contains serializer class for Custom User model
"""

from typing import Union
from rest_framework import serializers

from authentication.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializes User account model
    """
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        """
        Contains meta data of User Account serializer
        """
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'confirm_password')

    def create(self, validated_data: dict) -> 'CustomUser':
        """
        Create Custom User

        :param validated_data: Dictionary with required fields for Custom User
        :return: :class:`.CustomUser` object
        """
        return CustomUser.create(**validated_data)

    def validate(self, data: dict) -> Union[dict, bool]:
        """
        Check if CustomUser password is equal as password confirm

        :param data:
        :return: Custom User data, otherwise False
        """
        if data['password']:
            if data['password'] != data['confirm_password']:
                return False
        data.pop('confirm_password')
        return data
