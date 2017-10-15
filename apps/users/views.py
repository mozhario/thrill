from functools import reduce
from itertools import chain
from operator import attrgetter

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, FormView, UpdateView, DeleteView
from django.db.models import Q
from registration.views import RegistrationView
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import User, UserSubscription, UserPost
from .forms import UserRegistrationForm, UserEditForm
from apps.base.views import PostCreateView, PostEditView, PostAuthorRequiredMixin
from apps.communities.models import CommunityPost


class UserDetail(DetailView):
    model = User

    def get_object(self):
        try:
            user = User.objects.get(username=self.kwargs['username'])
            return user
        except ObjectDoesNotExist:
            raise Http404("We didn't found a person with username %s" % (self.kwargs['username']))



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
    form_class = UserRegistrationForm

    def register(self, form):
        user = form.save()

        group = Group.objects.get(name='User')
        user.groups.add(group)
        user.save()

        return redirect('auth_profile')


class UserEditView(LoginRequiredMixin, UpdateView):
    model_class = User
    form_class = UserEditForm
    template_name = 'users/user_edit.html'
    login_url = 'auth_login'
    success_url = 'user_edit'

    def get_object(self, *args, **kwargs):
        user = self.request.user
        return user


class SubscribeToUser(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        user_to_subscribe = User.objects.get(id=self.kwargs['user_id'])
        request.user.subscribe(user_to_subscribe)
        request.user.save()
        # TODO Json response
        return redirect(request.META.get('HTTP_REFERER', '/'))


class UnsubscribeFromUser(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        user_to_unsubscribe = User.objects.get(id=self.kwargs['user_id'])
        request.user.unsubscribe(user_to_unsubscribe)
        request.user.save()
        # TODO Json response
        return redirect(request.META.get('HTTP_REFERER', '/'))


class ProfileView(LoginRequiredMixin, View):
    login_url = 'auth_login'

    def get(self, request):
        return redirect('user_detail', request.user.username)


class UserPostCreateView(PostCreateView):
    model = UserPost
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect('user_post_detail', post.pk)


class UserPostEditView(PostAuthorRequiredMixin, PostEditView):
    model = UserPost
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=True)
        return redirect('user_post_detail', post.pk)


class UserPostDeleteView(PostAuthorRequiredMixin, LoginRequiredMixin, DeleteView):
    model = UserPost
    template_name = "posts/post_confirm_delete.html"
    success_url = 'profile'


class UserPostDetail(DetailView):
    model = UserPost
    template_name = 'posts/post_detail.html'


class UserPostList(ListView):
    model = UserPost
    template_name = 'posts/post_list.html'
    context_object_name = "posts_list"


# class UserFeed(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         # subscribed_to_users = filter(lambda x:  user.subscribed_to)
        
#         user_posts = UserPost.objects.filter(user__in=user.subscribed_to)
#         community_posts = CommunityPost.objects.filter(community__in=user.subscribed_to)

#         result_list = sorted(
#             chain(user_posts, community_posts),
#             key=attrgetter('created_at'),
#             reverse=True)

#         print(result_list)

#         return render(request, 'posts/post_list.html', {'posts_list': result_list})