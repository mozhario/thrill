from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^messages/$', views.ChatView.as_view(), name='messages'),
    # messages/username
    # messages/room/room_slug
]