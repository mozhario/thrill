from rest_framework import serializers

from apps.users.models import User, UserSubscription, UserPost
from apps.communities.models import Community, CommunityPost
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        filds = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'

    def validate(self, attrs):
        """
        Post must have atleast content or thumbnail pic
        """
        required_fields = dict()
        required_fields['content'] = attrs.get('content', None)
        required_fields['thumbnail'] = attrs.get('thumbnail', None)
        if self.instance:
            required_fields['instance_content'] = self.instance.content
            required_fields['instance_thumbnail'] = self.instance.content

        if not any(required_fields):
            raise serializers.ValidationError('Post should have atleast a content or thumbnail field filled.')

        return attrs


class UserPostSerializer(PostSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta(PostSerializer.Meta):
        model = UserPost


class CommunityPostSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        model = CommunityPost