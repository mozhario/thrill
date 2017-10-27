from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Count
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.db.models import Case, F, Sum, When, Max
from django.shortcuts import render

from apps.communities.models import Community
from apps.users.models import User, UserPost


def community_admin_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        try:
            key = int(kwargs['key'])
            community = Community.objects.get(pk=key)
        except ValueError:
            community = Community.objects.get(short_link=kwargs['key'])

        if community.admin != request.user:
            return HttpResponseForbidden("You are not allowed to manage this community.")
        else:
            return view_func(request, *args, **kwargs) 
  
    return _wrapped_view_func


class CommunityAdminRequiredMixin():
    '''
    Adds a check if logged in user is admin of a given communiy
    '''
    @method_decorator(community_admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CommunityAdminRequiredMixin, self).dispatch(request, *args, **kwargs)


def post_author_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        post = UserPost.objects.get(pk=kwargs['pk'])

        if post.user != request.user:
            return HttpResponseForbidden("You are not allowed to manage this post.")
        else:
            return view_func(request, *args, **kwargs) 
  
    return _wrapped_view_func


class PostAuthorRequiredMixin():
    '''
    Adds a check if logged in user is author of a given post
    '''
    @method_decorator(post_author_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PostAuthorRequiredMixin, self).dispatch(request, *args, **kwargs)


class Trending(View):
    def get(self, request, *args, **kwargs):
        posts = UserPost.objects \
                    .annotate(hype_ratio=(
                        Cast(F('likes_count'), output_field=FloatField() ) / Cast(Count('user__subscriptions'), output_field=FloatField()) ),
                    ).order_by('-hype_ratio')[:10]

        # posts = UserPost.objects.annotate(hype_ratio=Max('likes_count')).order_by('-likes_count')
        # print(posts.query)
        # print([post.hype_ratio for post in posts])
        return render(request, 'posts/post_list.html', context={'posts_list': posts})