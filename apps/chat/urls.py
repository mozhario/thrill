from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^messages/$', views.ChatView.as_view(), name='messages'),
    # messages/username ???

    url(r'^messages/room/create/$', views.ChatRoomCreate.as_view(), name='chatroom_create'),
    url(r'^messages/room/(?P<pk>\d+)/$', views.ChatRoomView.as_view(), name='chat_room'),
]