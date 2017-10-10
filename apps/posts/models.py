from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.users.models import User
from apps.communities.models import Community
from apps.base.models import Post


class UserPost(Post):
	user = models.ForeignKey(User)


class CommunityPost(Post):
	community = models.ForeignKey(Community)
