from django.db.models.signals import post_save
from actstream import action
from apps.users.models import User, UserPost


def user_post_created_handler(sender, instance, created, **kwargs):
    action.send(instance, verb='was saved')

post_save.connect(user_post_created_handler, sender=MyModel)