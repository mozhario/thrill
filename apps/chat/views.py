from django.shortcuts import render
from django.views import View


class ChatView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chat/chat.html')