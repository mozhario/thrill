from django.conf.urls import url
from .views import UserDetail

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetail.as_view()),
]