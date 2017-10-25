from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from apps.base.models import Timestamps
from apps.base.models import Post
from apps.users.models import User, UserSubscription

class Community(Timestamps):
    title = models.CharField(max_length=140)
    short_link = models.CharField(max_length=40, null=True, blank=True) # TODO validate as username (maybe property)
    description = models.TextField(max_length=9999)
    avatar_pic = models.ImageField(blank=True)
    admin = models.ForeignKey(User)

    subscriptions = GenericRelation(UserSubscription)

    type='community'

    def short_link_or_id(self):
        return self.short_link or self.pk


class CommunityPost(Post):
    community = models.ForeignKey(Community)