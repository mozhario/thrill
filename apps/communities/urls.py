from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^community/posts/$', views.CommunityPostCreateView.as_view(), name='community_post_create'),
    url(r'^community/posts/(?P<pk>\d+)/$', views.CommunityPostDetail.as_view(), name='community_post_detail'),
]