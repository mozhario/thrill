from rest_framework import serializers

from apps.users.models import User, UserPost
from apps.communities.models import Community, CommunityPost
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'


class UserPostSerializer(PostSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta(PostSerializer.Meta):
        model = UserPost


class CommunityPostSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        model = CommunityPost