from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import UserManager as DefaultUserManager
from django.core.cache import cache

from apps.base.models import Post


class UserManager(DefaultUserManager):
    '''
    User model manager that adds subscribers to single objects
    as well as objects in querysets

    Usage:
        user.subscribers - contains objects of users that subscribed to user
        user.subscribed_to - contains objects of users that user is subscribed to
    '''

    # TODO refactor subscribers managing methods to return querysets instead of lists
    @staticmethod
    def _get_subscribers(obj):
        cache_key = 'user_{id}_subscribers'.format(id=obj.pk)
        subscribers = cache.get(cache_key, None)
        
        if subscribers is None:
            subscribers = [subscription.user for subscription in UserSubscription.objects.filter(object_id=obj.pk)]
            cache.set(cache_key, subscribers, 60 * 60)

        return subscribers

    @staticmethod
    def _get_subscribed_to(obj):
        cache_key = 'user_{id}_subscribed_to'.format(id=obj.pk)
        subscribed_to = cache.get(cache_key, None)

        if subscribed_to is None:
            subscribed_to = [subscription.content_object for subscription in UserSubscription.objects.filter(user_id=obj.pk)]
            cache.set(cache_key, subscribed_to, 60 * 60)

        return subscribed_to

    @staticmethod
    def _get_liked_objects(obj):
        cache_key = 'user_{id}_liked'.format(id=obj.pk)
        liked  = cache.get(cache_key, None)
        
        if liked == None:
            liked = [item.content_object for item in obj.like_set.all()]
            cache.set(cache_key, liked, 60 * 60)

        return liked

    def get(self, *args, **kwargs):
        obj = super(UserManager, self).get(*args, **kwargs)
        obj.subscribers = self._get_subscribers(obj)
        obj.subscribed_to = self._get_subscribed_to(obj)
        obj.liked_objects = self._get_liked_objects(obj)
        return obj


class User(AbstractUser):
    '''
    Custom user model that adds some account profile fieds
    '''
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    profile_pic = models.ImageField(blank=True)
    subscriptions = GenericRelation('UserSubscription')

    objects = UserManager()


class UserSubscription(models.Model):
	'''
	Relation between user and the entity he is subscribed to.
	'''
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	

class UserPost(Post):
    user = models.ForeignKey(User)