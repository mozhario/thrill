from django.db import models


class Community(models.Model):
	title = models.CharField(max_length=140)
	short_link = models.CharField(max_length=40, unique=True)
	description = models.CharField(max_length=9999)
	avatar_pic = models.ImageField(blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)