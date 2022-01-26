import json
from channels.generic.websocket import AsyncWebsocketConsumer;

class ChatRoomConsumer(AsyncWebsocketConsumer):
    #Cololcamos Async delante de Deff para crear una funcion asincrona para conectar 
    async def connect(self):
        
        #recolectamor la informacion de la url del archivo routing.py del app, en mi caso 'chaski'
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        #despues de recolectar el room_name lo colocamos dentro de la variable room_group_name 
        self.room_group_name = "chaski_%s" % self.room_name
        
        #Creamos grupo de chat y lo colocamos en espera junto con la opcion de aceptar coneccion 
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
    
    #desconectar
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
    #Recpetor del mensaje 
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # Informacion del mensaje
        message = text_data_json['message']
        # Usuario que envio el mensaje
        username = text_data_json['username']

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chatroom_message', 'message': message, 'username' : username,
        })

    #devolemos el mensaje 
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']


        await self.send(text_data=json.dumps({'message': message, 'username': username}))