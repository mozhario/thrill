from django.db import models
from apps.base.models import Timestamps
from apps.base.models import Post
from apps.users.models import User


class Community(Timestamps):
    title = models.CharField(max_length=140)
    short_link = models.CharField(max_length=40, unique=True, null=True, blank=True) # TODO validate as username (maybe property)
    description = models.CharField(max_length=9999)
    avatar_pic = models.ImageField(blank=True)
    admin = models.ForeignKey(User)


class CommunityPost(Post):
    community = models.ForeignKey(Community)