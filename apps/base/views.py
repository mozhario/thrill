from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostCreateView(LoginRequiredMixin, CreateView):
    fields = [
        'title',
        'content',
        'excerpt',
        'thumbnail'
    ]