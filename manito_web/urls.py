from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from manito.views import index, home
from. import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', index, name="index"),
    path('', home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('allauth.urls')),
    path("game/", views.game, name="game"),
    path("room/<int:room_id>/", views.room_detail, name="room_detail"),
    path("create-room/", views.create_room, name="create_room"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)