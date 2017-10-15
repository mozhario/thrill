from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponseForbidden
from django.utils.decorators import method_decorator

from apps.communities.models import Community
from apps.users.models import User, UserPost


class PostCreateView(LoginRequiredMixin, CreateView):
    fields = [
        'title',
        'content',
        'excerpt',
        'thumbnail'
    ]


class PostEditView(LoginRequiredMixin, UpdateView):
    fields = [
        'title',
        'content',
        'excerpt',
        'thumbnail'
    ]


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