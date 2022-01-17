from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import ListaUsuarios

 
urlpatterns = [
    path("inicio/", views.index, name="index"),
    path("usuarios/<str:room_name>/", views.room, name="room"),
    path("registro/", views.register, name="registro"),
    path("",LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/",LogoutView.as_view(), name="logout"),
    path("usuarios/",ListaUsuarios.as_view(), name="usuarios")
]