from django.db.models.signals import post_save
from actstream import action
from apps.communities.models import CommunityPost


def community_post_created_handler(sender, instance, created, **kwargs):
    if created:
        action.send(
            instance.community,
            target=instance,
            verb='created'
        )

post_save.connect(community_post_created_handler, sender=CommunityPost)