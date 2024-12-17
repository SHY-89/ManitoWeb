from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("subsignup/", views.signup, name="subsignup"),
    path("sublogin/", views.login, name="sublogin"),
    path("sublogout/", views.logout, name="sublogout"),
    path("subdelete/<int:pk>/", views.delete, name="subdelete"),
    path("subupdate/<int:pk>/", views.update, name="subupdate"),
]