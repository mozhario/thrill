from django.conf.urls import url
from .views import UserDetail, UserList

urlpatterns = [
    url(r'', UserList.as_view()),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetail.as_view()),
]