from rest_framework import serializers

from apps.users.models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    bio = serializers.CharField(max_length=500)
    location = serializers.CharField(max_length=30)
    birth_date = serializers.DateField()
    phone = serializers.CharField(max_length=12)
    profile_pic = serializers.CharField()


class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=140)
    content = serializers.CharField(max_length=9999)
    excerpt = serializers.CharField(max_length=300)
    thumbnail = serializers.ImageField()
    likes_count = serializers.IntegerField(default=0)


class UserPostSerializer(PostSerializer):
    user_id = serializers.IntegerField()


class CommunityPostSerializer(PostSerializer):
    community_id = serializers.IntegerField()