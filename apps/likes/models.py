from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    user = models.ForeignKey('users.User')
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


# TODO add a counter field to posts and comments models