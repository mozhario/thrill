from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import IntegrityError
from django.apps import apps

from . import services
from .models import Like


class LikeUnlike(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        model = apps.get_model(request.GET['model_label'])
        obj = model.objects.get(pk=request.GET['pk'])

        try:
            services.like(request.user, obj)
            return JsonResponse({'likes': obj.likes_count})
        except IntegrityError as e:
            # If already liked - unlike
            services.unlike(request.user, obj)
            return JsonResponse({'likes': obj.likes_count})