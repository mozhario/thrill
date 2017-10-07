from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import User


class UserDetail(DetailView):
    model = User

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user
