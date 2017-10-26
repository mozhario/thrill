from django.utils.deprecation import MiddlewareMixin
from django_redis import get_redis_connection


class UserOnlineMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated():
            key = 'user_online_{username}'.format(username=request.user.username)
            con = get_redis_connection("default")
            con.set(key, request.path, 5 * 60)