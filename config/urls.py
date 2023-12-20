from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.userapp.urls')),
    path('category/', include('apps.category.urls')),
    path('car/', include('apps.car.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
