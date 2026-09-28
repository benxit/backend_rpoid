from django.urls import path
from . import views

app_name = 'gimnasio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
]
