from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^comments/$', views.LikeUnlike.as_view(), name='like_unlike'),
]