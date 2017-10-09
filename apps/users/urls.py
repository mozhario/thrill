from django.conf.urls import url
from .views import UserDetail, UserList, UserEditView

urlpatterns = [
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/(?P<username>[\w.@+-]+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^settings/$', UserEditView.as_view(), name='user_edit'),
    # url(r'^settings/delete-account$', UserDeleteView.as_view(), name='user_settings_delete'),
]