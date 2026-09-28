from django.urls import path
from . import views

app_name = 'comida_chatarra'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
]
