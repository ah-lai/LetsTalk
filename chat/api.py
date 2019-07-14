from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from knox.models import AuthToken
from knox.auth import TokenAuthentication

from create_user.serializers import  UserSerializer
from .serializers import MessageSerializer, RecieverSerializer, SenderSerializer

class SendMessageAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    authentication_classes = (TokenAuthentication,)

    #Request will have the TOKEN(sender user_id), content, reciver user_id
    def post(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION', '')
        content =  request.headers['content']
        sender_userId =  request.headers['sender_Userid']

        serializer_message = MessageSerializer(data=content)
        serializer_message.is_valid(raise_exception=True)
        serializer_message.save()
        
        serializer_reciever = RecieverSerializer(data=token)
        serializer_reciever.is_valid(raise_exception=True)
        serializer_reciever.save()

        serializer_sender = SenderSerializer(data=sender_userId)
        serializer_sender.is_valid(raise_exception=True)
        serializer_reciever.save()

        return Response({
            'Successful message sent'      
        })