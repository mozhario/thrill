from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class UserManager(models.Manager):
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
        return [subscription.user for subscription in UserSubscription.objects.filter(object_id=obj.pk)]

    @staticmethod
    def _get_subscribed_to(obj):
        return [subscription.content_object for subscription in UserSubscription.objects.filter(user_id=obj.pk)]

    def get_queryset(self, *args, **kwargs):
        queryset = super(UserManager, self).get_queryset(*args, **kwargs)
        for obj in queryset:
            obj.subscribers = self._get_subscribers(obj)
            obj.subscribed_to = self._get_subscribed_to(obj)
        return queryset

    def get(self, *args, **kwargs):
        obj = super(UserManager, self).get(*args, **kwargs)
        obj.subscribers = self._get_subscribers(obj)
        obj.subscribed_to = self._get_subscribed_to(obj)
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

    def subscribe(self, obj):
        self.subscriptions.create(user_id=self.pk, content_object=obj)
        return self

    # TODO unsubscribe
    def unsubscribe(self, obj):
        pass


class UserSubscription(models.Model):
	'''
	Relation between user and the entity he is subscribed to.
	'''
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	