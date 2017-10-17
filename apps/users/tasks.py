from celery import shared_task

from django.core.cache import cache

from .models import User, UserSubscription


@shared_task
def update_user_subscribed_to_cache(user_id):
    user_subscribed_to = [subscription.content_object for subscription 
                            in UserSubscription.objects.filter(user_id=user_id)] 
    
    cache.set(
        'user_{id}_subscribed_to'.format(id=user_id),
        user_subscribed_to
    )

@shared_task
def update_user_subscribers_cache(user_id):
    second_user_subscribers = [subscription.user for subscription 
                                in UserSubscription.objects.filter(object_id=user_id)]

    cache.set(
        'user_{id}_subscribers'.format(id=user_id), 
        second_user_subscribers
    )