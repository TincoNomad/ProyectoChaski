from channels.auth import AuthMiddlewareStack;
from channels.routing import ProtocolTypeRouter, URLRouter;
import chaski.routing

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(URLRouter(chaski.routing.websocket_urlpatterns))
})

