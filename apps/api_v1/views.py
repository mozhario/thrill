from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from apps.users.models import User, UserPost
from apps.communities.models import  Community, CommunityPost
from django.contrib.auth.models import Group
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = serializers.UserPostSerializer


class CommunityPostViewSet(viewsets.ModelViewSet):
    queryset = CommunityPost.objects.all()
    serializer_class = serializers.CommunityPostSerializer


class SomeAuthProtectedView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted',
            'user': str(request.user)
        }
        return Response(content)
