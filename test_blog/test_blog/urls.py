"""
test_blog URL Configuration

"""
from django.conf.urls import url, include

urlpatterns = [
    url('^api/auth/', include('authentication.urls')),
    url('^api/news/', include('news.urls')),
    url(r'.*', include('home.urls')),

]
