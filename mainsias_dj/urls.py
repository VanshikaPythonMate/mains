from django.contrib import admin
from django.urls import path, include
import door
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('maintain/', admin.site.urls),
    path('api/', include('door.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
