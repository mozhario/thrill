from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    Custom user model that adds some account profile fieds
    '''
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    profile_pic = models.ImageField(blank=True)


class UserSubscription(models.Model):
	'''
	Relation between user and the entity he is subscribed to.
	'''
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')