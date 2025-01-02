from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)  # 방 이름
    mission = models.TextField()  # 미션 내용
    reveal_date = models.DateTimeField()  # 매니또 공개 일시
    participant_count = models.PositiveIntegerField()  # 참여 인원 수
    is_active = models.BooleanField(default=True)  # 진행 중 여부
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간

    def __str__(self):
        return self.name
