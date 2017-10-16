from .models import UserSubscription
from django.core.cache import cache


class UserUserSubscriptionManager():
    '''
    Service that manages user-to-user subscription/unsubscription
    '''
    @staticmethod
    def _update_caches(user, second_user):
        '''
        user - is user who (subscribes to / unsubscribes from) second_user.
        This method updates caches of user subscriptions and second users
        subscribers 
        '''
        user_subscribed_to = [subscription.content_object for subscription 
                                in UserSubscription.objects.filter(user_id=user.pk)] 

        second_user_subscribers = [subscription.user for subscription 
                                    in UserSubscription.objects.filter(object_id=second_user.pk)]

        cache.set(
            'user_{id}_subscribed_to'.format(id=user.pk),
            user_subscribed_to
        )

        cache.set(
            'user_{id}_subscribers'.format(id=second_user.pk), 
            second_user_subscribers
        )

    @staticmethod
    def subscribe(user, user_to_subscribe):
        '''
        Creates a subscription relation. 
        Subscribes a user to user_to_subscribe.
        '''
        user.subscriptions.create(user_id=user.pk, content_object=user_to_subscribe)
        UserUserSubscriptionManager._update_caches(user, user_to_subscribe)

    @staticmethod
    def unsubscribe(user, user_to_unsubscribe):
        '''
        Destroys a subscription relation.
        Unsubscribes a user from user_to_subscribe.
        '''
        subscription = UserSubscription.objects.filter(user=user, object_id=user_to_unsubscribe.id)
        subscription.delete()
        UserUserSubscriptionManager._update_caches(user, user_to_unsubscribe)


class UserCommunitySubscriptionManager():
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

    @staticmethod
    def unsubscribe(user, community_to_unsubscribe):
        '''
        Destroys a subscription relation.
        Unsubscribes a user from community_to_subscribe.
        '''
        subscription = UserSubscription.objects.filter(user=user, object_id=community_to_unsubscribe.id)
        subscription.delete()