from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Room, Mission
from .forms import RoomForm


class RoomListCreateView(View):
    def get(self, request):
        rooms = Room.objects.all()
        form = RoomForm()
        return render(request, 'rooms/list_create.html', {'rooms': rooms, 'form': form})
    
    def post(self, request):
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save()  # 방 저장
            return redirect('room_detail', pk=room.pk)  # 새로 생성된 방의 상세 페이지로 리다이렉트
        rooms = Room.objects.all()  # 모든 방을 가져오기
        return render(request, 'rooms/list_create.html', {'rooms': rooms, 'form': form})



class RoomDetailView(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)  # URL에서 pk로 해당 방을 가져오기
        missions = Mission.objects.filter(room=room)  # 해당 방에 속한 미션들
        return render(request, 'rooms/detail.html', {'room': room, 'missions': missions})