from django.db import models

from apps.users.models import User
from apps.communities.models import Community
from apps.base.models import Post


class UserPost(Post):
	user = models.ForeignKey(User)


class CommunityPost(Post):
	community = models.ForeignKey(Community)
