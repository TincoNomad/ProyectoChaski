from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Usuario
from .forms import UserRegisterForm


def index(request):
    return render(request,"index.html", {}) 


def room(request, room_name, user = None):
    room_name = None
    if user is not None:
        room_name = Usuario.objects.get(user = user) 
    user = Usuario.objects.all()
    return render(request, "chatroom.html", {"room_name":room_name , "object_list": user})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    
    else:
        form = UserRegisterForm()

    return render(request,"register.html",{ "form":form})


class ListaUsuarios(ListView):
    model = Usuario
    
