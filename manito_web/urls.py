from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', index, name="index"),
    path('accounts/', include('accounts.urls')),
    path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)