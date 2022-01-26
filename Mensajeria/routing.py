#Protocolo de las rutas para los canales, ademas que vamos a identificar a los usuarios que manden los mensajes 
#hay que importar el archivo routing.py de el app, en mi caso 'chaski'
from channels.auth import AuthMiddlewareStack;
from channels.routing import ProtocolTypeRouter, URLRouter;
import chaski.routing


application = ProtocolTypeRouter({
    #Url de la ruta 
    'websocket': AuthMiddlewareStack(URLRouter(chaski.routing.websocket_urlpatterns))
})

