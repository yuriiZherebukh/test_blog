from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from news.serializers import NewsSerializer
from news.models import News


class NewsView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, news_id=None, format=None):
        if news_id:
            news = News.get_by_id(news_id)
            if not news:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = NewsSerializer(news)
            return Response(serializer.data)
        all_news = News.objects.all()
        response = NewsSerializer(all_news, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, news_id, format=None):
        news = News.get_by_id(news_id)
        if not news:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, news_id, format=None):
        news = News.get_by_id(news_id)
        if not news:
            return Response(status=status.HTTP_404_NOT_FOUND)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
