from django.apps import AppConfig


class CommunitiesConfig(AppConfig):
    name = 'communities'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Community'))
        registry.register(self.get_model('CommunityPost'))

        import .signals.handlers
