from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class Timestamps(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Post(Timestamps):
	title = models.CharField(max_length=140, blank=True)
	content = models.TextField(max_length=9999, blank=True)
	excerpt = models.TextField(max_length=300, blank=True)
	thumbnail = models.ImageField(blank=True)
	likes_count = models.PositiveIntegerField(default=0)

	likes = GenericRelation('likes.Like')
	comments = GenericRelation('comments.Comment')

	def model_label(self):
		return "{app_label}.{class_name}".format(
			app_label=self._meta.app_label,
			class_name=self.__class__.__name__
		)

	class Meta:
		abstract = True