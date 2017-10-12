from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.base.views import PostCreateView
from .models import CommunityPost




class CommunityPostCreateView(PostCreateView):
    model = CommunityPost
    

class CommunityPostDetail(DetailView):
    model = CommunityPost