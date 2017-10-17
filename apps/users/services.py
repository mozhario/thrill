from .models import UserSubscription
from django.core.cache import cache
from . import tasks



class BaseUserSubscriptionManager():
    @staticmethod
    def _update_user_subscribed_to_cache(user):
        tasks.update_user_subscribed_to_cache.delay(user.pk)

    @staticmethod
    def _update_user_subscribers_cache(user):
        tasks.update_user_subscribers_cache.delay(user.pk)
        


class UserUserSubscriptionManager(BaseUserSubscriptionManager):
    '''
    Service that manages user-to-user subscription/unsubscription
    '''
    @staticmethod
    def subscribe(user, user_to_subscribe):
        '''
        Creates a subscription relation. 
        Subscribes a user to user_to_subscribe.
        '''
        user.subscriptions.create(user_id=user.pk, content_object=user_to_subscribe)
        UserUserSubscriptionManager._update_user_subscribed_to_cache(user)
        UserUserSubscriptionManager._update_user_subscribers_cache(user_to_subscribe)

    @staticmethod
    def unsubscribe(user, user_to_unsubscribe):
        '''
        Destroys a subscription relation.
        Unsubscribes a user from user_to_subscribe.
        '''
        subscription = UserSubscription.objects.filter(user=user, object_id=user_to_unsubscribe.id)
        subscription.delete()
        UserUserSubscriptionManager._update_user_subscribed_to_cache(user)
        UserUserSubscriptionManager._update_user_subscribers_cache(user_to_unsubscribe)


class UserCommunitySubscriptionManager(BaseUserSubscriptionManager):
    '''
    Service that manages user-to-community subscription/unsubscription
    '''
    @staticmethod
    def subscribe(user, community_to_subscribe):
        '''
        Creates a subscription relation. 
        Subscribes a user to community_to_subscribe.
        '''
        user.subscriptions.create(user_id=user.pk, content_object=community_to_subscribe)
        UserUserSubscriptionManager._update_user_subscribed_to_cache(user)

    @staticmethod
    def unsubscribe(user, community_to_unsubscribe):
        '''
        Destroys a subscription relation.
        Unsubscribes a user from community_to_subscribe.
        '''
        subscription = UserSubscription.objects.filter(user=user, object_id=community_to_unsubscribe.id)
        subscription.delete()
        UserUserSubscriptionManager._update_user_subscribed_to_cache(user)