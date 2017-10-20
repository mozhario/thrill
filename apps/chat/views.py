from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import Message, Room


class ChatView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chat/chat.html')


class ChatRoomView(View):
    def get(self, request, *args, **kwargs):
        room = Room.objects.get(pk=self.kwargs['pk'])
        messages = room.message_set.order_by('-created_at')[:50]

        return render(request, 'chat/chat.html', context={
            'room': room,
            'messages': messages,
        })


class ChatRoomCreate(CreateView):
    model = Room
    fields = ['title', 'users']
    template_name = 'chat/chat_room_form.html'
    
    # def form_valid(self, form):
    #     return super(ChatRoomCreate, self).form_valid(form)


