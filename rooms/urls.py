from django.urls import path
from . import views

urlpatterns = [
	path("", views.RoomListCreateView.as_view(), name="room_list_create"), #list와 create를 하나로 묶고
	path("rooms/<int:pk>/", views.RoomDetailView.as_view(), name="room_detail"), #디테일 관련 안에 메서드로 처리
	#디테일만 따로 묶어야 url이 하나로 나올 수 있다. 효율적인 url
	]