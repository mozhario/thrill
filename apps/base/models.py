from django.db import models


class Timestamps(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Post(Timestamps):
	title = models.CharField(max_length=140)
	content = models.CharField(max_length=9999)
	excerpt = models.CharField(max_length=300, blank=True)
	thumbnail = models.ImageField(blank=True)

	class Meta:
		abstract = True