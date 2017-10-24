from celery import shared_task

from django.core.cache import cache

from .models import Like


@shared_task
def update_user_liked_objects_cache(user_id):
    liked_objects = [item.content_object for item 
                            in Like.objects.filter(user_id=user_id)]
    
    cache.set(
        'user_{id}_liked'.format(id=user_id),
        liked_objects
    )