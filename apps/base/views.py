from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponseForbidden
from django.utils.decorators import method_decorator

from apps.communities.models import Community


class PostCreateView(LoginRequiredMixin, CreateView):
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
    @method_decorator(community_admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CommunityAdminRequiredMixin, self).dispatch(request, *args, **kwargs)