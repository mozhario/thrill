from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden

from apps.base.views import PostCreateView, CommunityAdminRequiredMixin
from .models import Community, CommunityPost


class CommunityDetail(DetailView):
    model = Community

    def get_object(self):
        try:
            key = int(self.kwargs['key'])
            return Community.objects.get(pk=key)
        except ValueError:
            return Community.objects.get(short_link=self.kwargs['key'])


class CommunityList(ListView):
    model = Community
    context_object_name = 'communities'


class CommunityCreateView(LoginRequiredMixin, CreateView):
    model = Community
    fields = [
        'title',
        'short_link',
        'description',
        'avatar_pic',
    ]

    def form_valid(self, form):
        community = form.save(commit=False)
        community.admin = self.request.user # community here
        community.save()
        return redirect('community_detail', community.pk)


class CommunityPostCreateView(CommunityAdminRequiredMixin, PostCreateView):
    # TODO refactoring for:
    # 1. getting community object by url param in more generic way
    # 2. checking if user is admin of community should be a mixin or something

    model = CommunityPost
    template_name = 'posts/post_form.html'

    def get_object(self):
        try:
            key = int(self.kwargs['key'])
            community = Community.objects.get(pk=key)
        except ValueError:
            community = Community.objects.get(short_link=self.kwargs['key'])

        return community

    def form_valid(self, form):
        post = form.save(commit=False)

        community = self.get_object()

        post.community = community
        post.save()

        community_key = community.short_link or community.pk
  
        return redirect('community_post_detail', community_key, post.pk)
    

class CommunityPostDetail(DetailView):
    model = CommunityPost
    template_name = 'posts/post_detail.html'
