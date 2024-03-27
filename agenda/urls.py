from django.contrib import admin
from django.urls import path, include

from .views import *

from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', include('contact.urls')),
    path('task/', include('task.urls')),
    path('meetings/', include('meetings.urls')),
    path('travels/', include('travels.urls')),
    path('user/', include('user.urls')),
    path('about/', about_me, name="about"),
    path('<int:pk>/password/', ChangePassword.as_view(), name='change_password'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
