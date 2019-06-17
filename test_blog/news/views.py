"""
This module contains News View
"""

from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewsSerializer


class NewsView(APIView):
    """
    Perform operations to create, read, update and delete news
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request: Request, news_id: int = None, format=None) -> Response:
        """
        Handle GET HTTP Request

        :param request: Request object
        :param news_id: ID of News to get
        :param format: Whether use or not format suffixes
        :return: Response with JSON News data if request was handled successfully, otherwise Response
            with 404 status code
        """
        if news_id:
            news = News.get_by_id(news_id)
            if not news:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = NewsSerializer(news)
            return Response(serializer.data)
        all_news = News.objects.all()
        response = NewsSerializer(all_news, many=True)
        return Response(response.data)

    def post(self, request: Request, format=None) -> 'Response':
        """
        Handle POST HTTP Request

        :param request: Request object
        :param format: Whether use or not format suffixes
        :return: Response with JSON News data if News was successfully created, otherwise Response
            with 400 status code
        """
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, news_id, format=None) -> 'Response':
        """
        Handle PUT HTTP Request

        :param request: Request object
        :param news_id: ID of News to update
        :param format: Whether use or not format suffixes
        :return: Response with JSON News data if News was successfully updated, otherwise Response
            with 400 status code
        """
        news = News.get_by_id(news_id)
        if not news:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, news_id: int, format=None) -> 'Response':
        """
        Handle DELETE HTTP request

        :param request: Request
        :param news_id: ID of News to delete
        :param format: Whether use or not format suffixes
        :return: Response with JSON News data if News was successfully deleted, otherwise Response
            with 404 status code
        """
        news = News.get_by_id(news_id)
        if not news:
            return Response(status=status.HTTP_404_NOT_FOUND)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
