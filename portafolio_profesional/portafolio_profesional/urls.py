from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev1/', include('dev1.urls')),
    path('dev2/', include('dev2.urls')),
]
