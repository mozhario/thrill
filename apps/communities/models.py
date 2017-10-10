from django.db import models
from apps.base.models import Timestamps


class Community(Timestamps):
	title = models.CharField(max_length=140)
	short_link = models.CharField(max_length=40, unique=True)
	description = models.CharField(max_length=9999)
	avatar_pic = models.ImageField(blank=True)
