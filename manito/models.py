from django.db import models
from django.conf import settings

class Room(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_rooms",
    )
    name = models.CharField(max_length=100)
    mission = models.TextField()
    reveal_date = models.DateTimeField()
    participant_count = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
