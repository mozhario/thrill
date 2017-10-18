from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('User'))
        registry.register(self.get_model('UserPost'))

        import apps.users.signals.handlers
