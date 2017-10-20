from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Comment
from apps.users.models import UserPost
from apps.communities.models import CommunityPost


class CommentAdd(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post_type = request.POST['post-type']
        post_id = request.POST['post-id']
        content = request.POST['comment-content']

        if post_type == "user-post":
            post_model = UserPost
            reverse = 'user_post_detail'
        else:
            post_model = CommunityPost

        post = post_model.objects.get(pk=post_id)

        comment = Comment.objects.create(
            content=content,
            content_object=post,
            author=request.user
        )
        
        return redirect(request.META.get('HTTP_REFERER', '/'))