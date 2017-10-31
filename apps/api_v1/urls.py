from django.conf.urls import url, include
from rest_framework import routers
from . import views
from rest_framework.authtoken .views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'some/$', views.SomeAuthProtectedView.as_view()),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user-token/', obtain_auth_token),
]