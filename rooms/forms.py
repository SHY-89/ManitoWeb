from django import forms
from .models import Room, Mission

# Room 모델 폼
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'room_type', 'appear_data', 'headcount',]
        widgets = {
            'appear_data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # 날짜 및 시간 형식으로 입력 받기
        }
        labels = {
            "name": "마니또 방 이름",
            "room_type": "마니또 방 선택하기",
            "apper_data": "닉네임",
            "headcount": "인원 수",
        }

# Mission 모델 폼
class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['room', 'mission_type', 'custom_mission']
        widgets = {
            'custom_mission': forms.Textarea(attrs={'rows': 3, 'cols': 50}),  # 커스텀 미션을 입력하는 텍스트 영역
        }
