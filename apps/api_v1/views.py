from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import authentication

from apps.users.models import User, UserPost
from apps.users.services import UserUserSubscriptionManager
from apps.communities.models import  Community, CommunityPost
from django.contrib.auth.models import Group
from . import serializers
from .permissions import IsMeOrReadOnly, IsPostAuthorOrReadOnly, IsCommunityAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsMeOrReadOnly,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User Posts to be viewed or edited.
    """
    permission_classes = (IsPostAuthorOrReadOnly,)
    queryset = UserPost.objects.all()
    serializer_class = serializers.UserPostSerializer


class CommunityPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Community Posts to be viewed or edited.
    """
    permission_classes = (IsCommunityAdminOrReadOnly,)
    queryset = CommunityPost.objects.all()
    serializer_class = serializers.CommunityPostSerializer


# TODO: refactor to more generic way (subscribe-unsubscribe)
class UserSubscribeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        performer_id = request.GET.get('performer_id', None)
        object_id = request.GET.get('object_id', None)
        if not any((performer_id, object_id)):
            pass # TODO raise something or return error

        performer = User.objects.get(pk=performer_id)
        obj = User.objects.get(pk=object_id)
        UserUserSubscriptionManager.subscribe(performer, obj)
        serialized_performer = serializers.UserSerializer(performer)

        return Response({
            'performer': serialized_performer.data,
            'action': '%s subscribed to %s' % (performer.username, obj.username)
        })


class UserUnsubscribeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        performer_id = request.GET.get('performer_id', None)
        object_id = request.GET.get('object_id', None)
        if not any((performer_id, object_id)):
            pass  # TODO raise something or return error

        performer = User.objects.get(pk=performer_id)
        obj = User.objects.get(pk=object_id)
        UserUserSubscriptionManager.unsubscribe(performer, obj)
        serialized_performer = serializers.UserSerializer(performer)

        return Response({
            'performer': serialized_performer.data,
            'action': '%s unsubscribed from %s' % (performer.username, obj.username)
        })


class SomeAuthProtectedView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted',
            'user': str(request.user)
        }
        return Response(content)