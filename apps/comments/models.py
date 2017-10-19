from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# from apps.users.models import User
from apps.base.models import Timestamps


class Comment(Timestamps):
    author = models.ForeignKey('users.User')
    content = models.TextField(max_length=240)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')