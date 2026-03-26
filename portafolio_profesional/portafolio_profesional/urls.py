from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. ESTO ES EL MENÚ DE LOS 4 (Landing Page)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # 2. CADA UNO EN SU PROPIA RUTA
    path('dev1/', include('dev1.urls')),
    path('dev2/', include('dev2.urls')),
    path('dev3/', include('dev3.urls')),
    
    # IMPORTANTE: Verifica que Andrés NO tenga path('', include("dev4.urls"))
    path('dev4/', include('dev4.urls')), 
]