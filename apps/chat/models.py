from django.db import models
from apps.base.models import Timestamps


class Message(Timestamps):
    user = models.ForeignKey('users.User')
    text = models.TextField(max_length=3000)
    room = models.ForeignKey('chat.Room')


class Room(Timestamps):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField('users.User')