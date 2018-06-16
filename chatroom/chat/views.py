import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from chat.models import ChatRoom, Message


@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'chat/index.html')
    elif request.method == 'POST':
        form = request.POST.dict()
        roomname = form.get('roomname').lower().replace(
            ' ', '-'
        )
        chatroom, created = ChatRoom.objects.get_or_create(
            name=roomname,
        )
        doc = {
            'roomname': chatroom.name,
        }
        return JsonResponse(doc)


@login_required
def room(request, room_name):
    chatroom = ChatRoom.objects.get(
        name=room_name
    )
    messages = Message.objects.filter(
        author=request.user,
        chatroom=chatroom,
    ).order_by('timestamp')[:30]
    context = {
        'messages': messages,
        'user_pk': request.user.pk,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    return render(request, 'chat/room.html', context)
