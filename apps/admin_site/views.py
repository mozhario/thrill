import re

from django.shortcuts import render

from django_redis import get_redis_connection


def online_users(request):
    con = get_redis_connection("default")

    username = re.compile(r"user_online_([a-zA-Z0-9_]*)")

    users = {}
    for key in con.scan_iter('user_online_*'):
        username = username.search(key.decode('utf-8')).group(1)
        users[username] = con.get(key).decode('utf-8')

    return render(request, 'admin/users_online.html', context={
        'users': users
    })