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
        reciever_userId =  request.headers['reciever_userId']

        serializer_message = MessageSerializer(data=content)
        serializer_message.is_valid(raise_exception=True)
        serializer_message.save() #create an instance of a message (?)

        # or should just make get_object



        try:
            user_sender = message_sender.get_object(token) #we put the sender id
        except user_sender.DoesNotExist:
            print(xxx)
            # create the user object (sender & reciever)

        try:
            user_reciever = message_reciever.get_object(reciever_userId) #we put the reciever id
        except user_reciever.DoesNotExist:
            print(xxx)
            # create the user object (sender & reciever)

        serializer_reciever = RecieverSerializer(instance=user_sender)
        serializer_reciever.is_valid(raise_exception=True)
        serializer_reciever.save()

        serializer_sender = SenderSerializer(instance=user_reciever)
        serializer_sender.is_valid(raise_exception=True)
        serializer_reciever.save()

        return Response({
            'Successful message sent'
        })
