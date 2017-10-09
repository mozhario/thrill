from functools import reduce

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.db.models import Q
from registration.views import RegistrationView
from django.contrib.auth.models import Group

from .models import User
from .forms import UserForm


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

        search_query = self.request.GET.get('s_query')

        if search_query:
            query_terms = search_query.split()
            users = users.filter(
                # First name contains any word from search query OR
                reduce(lambda x, y: x | y, [Q(first_name__icontains=item) for item in query_terms]) |
                # Last name contains any word from search query OR
                reduce(lambda x, y: x | y, [Q(last_name__icontains=item) for item in query_terms]) |
                # Username contains any word from search query
                reduce(lambda x, y: x | y, [Q(username__icontains=item) for item in query_terms])
            )

        return users


class UserRegistrationView(RegistrationView):
    form_class = UserForm

    def register(self, form):
        user = form.save()

        group = Group.objects.get(name='User')
        user.groups.add(group)
        user.save()

        return redirect('auth_profile')