'''
Service that operates generic like/unlike actions.
'''
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from .models import Like


def increment_likes_count(obj):
    '''
    Increments entity likes_count attribute if entity is supporting
    such interface. Ohterwise does nothing.
    '''
    try:
        obj.likes_count = obj.likes_count + 1
        obj.save()
    except AttributeError:
        pass

def decrement_likes_count(obj):
    '''
    Decrements entity likes_count attribute if entity is supporting
    such interface and it's likes counter is > 0. Ohterwise does nothing.
    '''
    try:
        if obj.likes_count > 0:
            obj.likes_count = obj.likes_count - 1
            obj.save()
    except AttributeError:
        pass


def like(user, obj):
    '''
    Creates a like relation between the user and object
    '''
    like = Like.objects.create(
        user=user,
        content_object=obj
    )
    increment_likes_count(obj)


def unlike(user, obj):
    '''
    Destroys a like relation between the user and object
    '''
    try:
        obj_content_type = ContentType.objects.get_for_model(obj)
        like = Like.objects.get(
            user=user,
            content_type=obj_content_type.id,
            object_id=obj.pk
        )
        like.delete()
        decrement_likes_count(obj)

    except ObjectDoesNotExist:
        pass