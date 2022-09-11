from django.shortcuts import render
from django.http import Http404

from .models import Room

rooms = [
    {"id": 1, "name": "Pierwszy"},
    {"id": 2, "name": "Drugi"},
    {"id": 3, "name": "Trzeci"}
]


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        raise Http404
    context = {"room": room}
    return render(request, 'base/room.html', context)
