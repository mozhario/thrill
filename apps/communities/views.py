from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from apps.base.views import PostCreateView
from .models import Community, CommunityPost


class CommunityDetail(DetailView):
    model = Community

    def get_object(self):
        short_link = self.kwargs.get('short_link', None)
        pk = self.kwargs.get('pk', None)

        if short_link:
            community = Community.objects.get(short_link=short_link)
            return community
        elif pk:
            community = Community.objects.get(pk=pk)
            return community
        else:
            raise Http404("We didn't found such a community.")


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


class CommunityPostCreateView(PostCreateView):
    model = CommunityPost
    template_name = 'posts/post_form.html'
    # TODO implement 
    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.user = self.request.user # community here
    #     post.save()
    #     return redirect('user_post_detail', post.pk)
    

class CommunityPostDetail(DetailView):
    model = CommunityPost
    template_name = 'posts/post_detail.html'
