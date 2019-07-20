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
        serializer_message.save() #create an instance of a message object


        # Obtain the user_sender/reciever objects using the foreign key which is linked to the User (?)
        #  Question: if we have a foreign key between user ID and user_sender ID (is the user sender object create when user is created?)
        try:
            user_sender = message_sender.objects.get(user_id=token) #we need to get user id from token (right now this line is wrong)
            user_reciever = message_reciever.objects.get(user_id=reciever_userId)
        expect: 
            return Response({
                'Error of finding user'
            })

            
        # we use the serializer to link the message with the user object (?)
        # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships 
        # first example shows how the nested  
        
        serializer_reciever = RecieverSerializer(instance=user_sender, message=serializer_message)
        serializer_reciever.is_valid(raise_exception=True)
        serializer_reciever.save()

        serializer_sender = SenderSerializer(instance=user_reciever, message=serializer_message)
        serializer_sender.is_valid(raise_exception=True)
        serializer_reciever.save()

        return Response({
            'Successful message sent'
        })
