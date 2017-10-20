from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^comments/add/$', views.CommentAdd.as_view(), name='comment_add'),
]