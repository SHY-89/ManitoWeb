from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Room(models.Model):
    name = models.CharField(max_length=100)  # 방 이름
    is_active = models.BooleanField(default=True)  # 진행 여부

    def __str__(self):
        return self.name
