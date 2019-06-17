"""
This module contains AuthRegister View to register user
"""

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import CustomUserSerializer


class AuthRegister(APIView):
    """
    Contains functionality to register user
    """

    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, format=None) -> 'Response':
        """
        Handle POST HTTP request to create Custom user

        :param request: Request object
        :param format: Whether use or not format suffixes
        :return: Response with JSON News data if User was successfully created, otherwise Response
            with 400 status code
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.validate(request.data):
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
