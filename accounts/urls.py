from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("subsignup/", views.signup, name="subsignup"),
    path("sublogin/", views.login, name="sublogin"),
    path("sublogout/", views.logout, name="sublogout"),
    path("subdelete/<int:pk>/", views.delete, name="subdelete"),
    path("subupdate/<int:pk>/", views.update, name="subupdate"),

    path("login/", views.sociallogin, name="sociallogin"), 
    path("kakao/login/callback/", views.kakaos, name="kakaos"),
    path('google/login/callback/', views.google_callback, name='google_callback'),
    path('naver/login/callback/', views.naver_callback, name='naver_callback'),
    path("", views.home, name="home"),
]