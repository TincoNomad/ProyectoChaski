from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import ListaUsuarios


urlpatterns = [
    #inicio 
    path('inicio/', views.index, name='index'),
    #ChatRoom
    path('usuarios/<str:room_name>/', views.room, name='room'),
    #Formulario de registro
    path('registro/', views.register, name='registro'),
    #Formulario para ingreras colocado como vista de inicio 
    path('',LoginView.as_view(template_name='login.html'), name='login'),
    #Planilla preprogramada de Django para salir 
    path('logout/',LogoutView.as_view(), name='logout'),
    #lista de usuarios 
    path('usuarios/',ListaUsuarios.as_view(), name='usuarios'),
]