from django.shortcuts import render
from django.http import Http404

rooms = [
    {"id": 1, "name": "Pierwszy"},
    {"id": 2, "name": "Drugi"},
    {"id": 3, "name": "Trzeci"}
]


def home(request):
    context = {"rooms": rooms}
    return render(request, 'base/home.html', context)


def room(request, id):
    room = None
    for i in rooms:
        if i.get("id", None) == id:
            room = i
    if room is None:
        raise Http404
    context = {"room": room}
    return render(request, 'base/room.html', context)