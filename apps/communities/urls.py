from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^communities/$', views.CommunityList.as_view(), name='community_list'),
    url(r'^communities/create/$', views.CommunityCreateView.as_view(), name='community_create'),
    url(r'^communities/(?P<key>[\d|\w.@+-]+)/edit/$', views.CommunityEditView.as_view(), name='community_edit'),
    url(r'^communities/(?P<key>[\d|\w.@+-]+)/$', views.CommunityDetail.as_view(), name='community_detail'),

    url(r'^communities/(?P<community_id>\d+)/subscribe/$', views.SubscribeToCommunity.as_view(), name='community_subscribe'),
    url(r'^communities/(?P<community_id>\d+)/unsubscribe/$', views.UnsubscribeFromCommunity.as_view(), name='community_unsubscribe'),

    url(r'^c/(?P<key>[\d|\w.@+-]+)/posts/create/$', views.CommunityPostCreateView.as_view(), name='community_post_create'),
    url(r'^c/(?P<key>[\d|\w.@+-]+)/posts/(?P<pk>\d+)/$', views.CommunityPostDetail.as_view(), name='community_post_detail'),
]