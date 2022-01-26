from django.urls import re_path;
from . import consumers;

websocket_urlpatterns = [
    #Colocamos los parametros generales de donde se encuetra la url y utilizamos una url dinamica donde consumer
    #funciona como Views y ChatRoomConsumer es una clase 
    # .as_agui es lo que conecta la url con el servidor local
    # La W+ empareja y recive cualqueir letra en mayuscula o minuscula o numero y el signo como parte del url 
    # y el dolar marca el final del end point de la url 
    re_path(r'ws/chaski/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]