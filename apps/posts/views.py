from django.shortcuts import render, redirect

from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserPost, CommunityPost


class PostCreateView(LoginRequiredMixin, CreateView):
    fields = [
        'title',
        'content',
        'excerpt',
        'thumbnail'
    ]


class UserPostCreateView(PostCreateView):
    model = UserPost

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect('user_post_detail', post.pk)


class UserPostList(ListView):
    model = UserPost
    context_object_name = "posts_list"


class CommunityPostCreateView(PostCreateView):
    model = CommunityPost


class UserPostDetail(DetailView):
    model = UserPost


class CommunityPostDetail(DetailView):
    model = CommunityPost