'''
Service that operates generic like/unlike actions.
'''

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


def like(user, obj):
    '''
    Creates a like relation between the user and object
    '''
    like = Like.objects.create(
        user=user,
        content_object=obj
    )
    increment_likes_count(obj)

