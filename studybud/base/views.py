from django.shortcuts import render, redirect
from django.http import Http404, request
from .models import Room
from .forms import RoomForm

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


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})