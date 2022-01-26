
from django.contrib import admin;
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Urls del App
    path('',include('chaski.urls')),
];
