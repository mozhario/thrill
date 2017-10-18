from django.apps import AppConfig


class CommunitiesConfig(AppConfig):
    name = 'apps.communities'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Community'))
        registry.register(self.get_model('CommunityPost'))

        import apps.communities.signals.handlers