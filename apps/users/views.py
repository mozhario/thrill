from functools import reduce

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.db.models import Q

from .models import User


class UserDetail(DetailView):
    model = User

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user

class UserList(ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 50

    def get_queryset(self):
        users = User.objects.all()
        return users