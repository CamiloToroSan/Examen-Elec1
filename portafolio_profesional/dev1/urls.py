from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoja_vida, name='hoja_vida_dev1'),
]