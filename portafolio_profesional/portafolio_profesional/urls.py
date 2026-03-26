from django.contrib import admin
from django.urls import path, include  # Importante agregar 'include'
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Menú Principal (La raíz del sitio)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # 2. Rutas de los 4 integrantes (Consolidación)
    path('dev1/', include('dev1.urls')),
    path('dev2/', include('dev2.urls')),
    path('dev3/', include('dev3.urls')),
    path('dev4/', include('dev4.urls')),
]