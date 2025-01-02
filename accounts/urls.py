from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("subsignup/", views.signup, name="subsignup"),
    path("sublogin/", views.login, name="sublogin"),
    path("sublogout/", views.logout, name="sublogout"),
    path("subdelete/<int:pk>/", views.delete, name="subdelete"),
    path("subupdate/<int:pk>/", views.update, name="subupdate"),

    path("kakao/", views.kakao, name="kakao"), 
    path("game/", views.game, name="game"),
    path("room/<int:room_id>/", views.room_detail, name="room_detail"),
    path("create-room/", views.create_room, name="create_room"),
]