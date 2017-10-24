from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import IntegrityError

from . import services
from .models import Like


class LikeUnlikeBase(LoginRequiredMixin, View):
    '''
    It's a base view that should be implemented with pointing out
    some specific model
    '''
    model = None

    def get(self, request, *args, **kwargs):
        obj = self.model.objects.get(pk=kwargs['pk'])

        try:
            services.like(request.user, obj)
            return JsonResponse({'likes': obj.likes_count})
        except IntegrityError as e:
            # If already liked - unlike
            services.unlike(request.user, obj)
            return JsonResponse({'likes': obj.likes_count})