from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from authentication.views import AuthRegister

urlpatterns = [
    url(r'^api-token-auth/$', obtain_jwt_token),
    url(r'^api-token-refresh/$', refresh_jwt_token),
    url(r'^register/$', AuthRegister.as_view()),
]
