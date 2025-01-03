from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .models import Room
from django.contrib import messages
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm


def game(request):
    # 진행 중인 방만 가져오기
    ongoing_rooms = Room.objects.filter(is_active=True)  # is_active=True 조건으로 필터링
    return render(request, 'manito/game.html', {'ongoing_rooms': ongoing_rooms})


def create_room(request):
    if request.method == "POST":
        room_type = request.POST.get("room_type")
        mission = request.POST.getlist("missions[]")  # 미션 배열
        reveal_date = request.POST.get("reveal_date")
        participant_count = request.POST.get("participant_count")
        
        # 참여 인원수 검증
        if int(participant_count) < 3:
            messages.error(request, "참여 인원수는 최소 3명 이상이어야 합니다.")
            return render(request, 'manito/create_room.html')

        # Room 모델에 저장
        Room.objects.create(
            name=room_type,
            mission=", ".join(mission),  # 미션을 쉼표로 구분해서 저장
            reveal_date=reveal_date,
            participant_count=int(participant_count),
            is_active=True
        )
        messages.success(request, "마니또 방이 성공적으로 생성되었습니다.")
        return redirect('manito:game')

    return render(request, 'manito/create_room.html')


def room_detail(request, room_id):
    # 특정 방의 정보를 가져오기
    room = get_object_or_404(Room, id=room_id)
    return render(request, "manito/room_detail.html", {"room": room})
