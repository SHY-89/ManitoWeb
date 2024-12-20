from django.db import models

# 방 모델

class Room(models.Model):
    ROOM_TYPES = [
        ("mission", "미션 마니또"),
        ("goodjob", "칭찬 마니또"),
        ("gift", "선물 마니또"),
    ]

    name = models.CharField(max_length=50)  # 방 이름
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)  # 방 유형
    appear_data = models.DateTimeField()  # 마니또 공개 일시
    headcount = models.PositiveIntegerField(default=3)  # 인원 수 (최소 3명)
    def __str__(self):
        return self.name


# 미션 모델
class Mission(models.Model):
    MISSION_TYPES = [
        ("커피", "커피 사주기"),
        ("칭찬", "칭찬 쪽지 몰래 두기"),
        ("간식", "간식 선물 하기"), 
        ("책상", "책상 정리 해주기"),
        ("도움", "소소한 도움 주기"),
        ("초상화", "초상화 그려주기"),
        ("손편지", "손편지 써주기"),
        ("사진", "사진 찍기"),
        ("삼행시", "3행시 짓기"),
        ("기타", "기타")
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='missions')  # Room과 연결
    mission_type = models.CharField(max_length=20, choices=MISSION_TYPES)  # 미션 유형
    custom_mission = models.TextField(blank=True, null=True)  # 사용자가 직접 입력한 미션 (선택적)

    def __str__(self):
        # 미션 유형을 항상 반환하고, 추가적으로 사용자가 입력한 미션이 있으면 그 내용을 추가로 표시
        return f"{self.mission_type} - {self.custom_mission}" if self.custom_mission else self.mission_type
    

class image(models.Model):
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)  # 이미지 업로드
