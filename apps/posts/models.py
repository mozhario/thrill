from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
	title = models.CharField(max_length=140)
	content = models.CharField(max_length=9999)
	excerpt = models.CharField(max_length=300, blank=True)
	# TODO: author id (can be user or community)

	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')