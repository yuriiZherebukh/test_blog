from news.views import NewsView

from django.conf.urls import url

urlpatterns = [
    url(r'^$', NewsView.as_view()),
    url(r'^(?P<news_id>\d+)/$', NewsView.as_view()),
    ]
