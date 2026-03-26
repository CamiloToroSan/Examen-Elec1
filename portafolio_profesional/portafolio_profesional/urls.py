from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev1/', include('dev1.urls')),
    path('dev2/', include('dev2.urls')),
    path('dev3/', include("dev3.urls")), 
    path('dev4/', include("dev4.urls")),
]
