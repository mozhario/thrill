from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps

from .models import Comment
from apps.users.models import UserPost
from apps.communities.models import CommunityPost


class CommentAdd(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post_type = request.POST['post-type']
        post_id = request.POST['post-id']
        content = request.POST['comment-content']

        post_model = apps.get_model(post_type)
        post = post_model.objects.get(pk=post_id)

        comment = Comment.objects.create(
            content=content,
            content_object=post,
            author=request.user
        )
        
        return redirect(request.META.get('HTTP_REFERER', '/'))


class CommentReply(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST['comment-id']
        comment_content = request.POST['comment-content']

        comment = Comment.objects.get(pk=comment_id)
        post = comment.content_object

        reply = Comment.objects.create(
            content=comment_content,
            content_object=post,
            parent=comment,
            author=request.user
        )
        
        return redirect(request.META.get('HTTP_REFERER', '/'))