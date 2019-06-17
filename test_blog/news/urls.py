"""
URL Routes to News app
"""

from django.conf.urls import url

from news.views import NewsView

urlpatterns = [
    url(r'^$', NewsView.as_view()),
    url(r'^(?P<news_id>\d+)/$', NewsView.as_view()),
]
