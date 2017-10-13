from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^communities/$', views.CommunityList.as_view(), name='community_list'),
    url(r'^communities/create/$', views.CommunityCreateView.as_view(), name='community_create'),
    url(r'^communities/(?P<pk>\d+)/$', views.CommunityDetail.as_view(), name='community_detail'),
    url(r'^communities/(?P<short_link>[\w.@+-]+)/$', views.CommunityDetail.as_view(), name='community_detail'),

    url(r'^c/(?P<community_id>\d+)/posts/create/$', views.CommunityPostCreateView.as_view(), name='community_post_create'),
    url(r'^c/(?P<community_id>\d+)/posts/(?P<pk>\d+)/$', views.CommunityPostDetail.as_view(), name='community_post_detail'),
    url(r'^c/(?P<short_link>[\w.@+-]+)/posts/create/$', views.CommunityPostCreateView.as_view(), name='community_post_create'),
    url(r'^c/(?P<short_link>[\w.@+-]+)/posts/(?P<pk>\d+)/$', views.CommunityPostDetail.as_view(), name='community_post_detail'),
]