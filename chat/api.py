from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from knox.models import AuthToken
from knox.auth import TokenAuthentication

from create_user.serializers import  UserSerializer
from .serializers import MessageSerializer, RecieverSerializer, SenderSerializer

from .models import message_sender, message, message_reciever

class SendMessageAPI(APIView):
    permission_classes = [permissions.AllowAny, ]
    authentication_classes = (TokenAuthentication,)

    #Request will have the TOKEN(sender user_id), content, reciver user_id
    def post(self, request, *args, **kwargs):

        #token = request.META.get('HTTP_AUTHORIZATION', '')

        senderID = request.POST.get('senderID')
        content =  request.POST.get('content')
        recieverID =  request.POST.get('recieverID')

        print(content)

        # Obtain the user_sender/reciever objects using the foreign key which is linked to the User (?)
        
        try:
            user_reciever = message_reciever.objects.get(pk=senderID) 
        except:
            user_reciever = message_reciever.objects.create(pk=senderID) 

        try:
            user_sender = message_sender.objects.get(pk=recieverID)
        except:
            user_sender = message_sender.objects.create(pk=recieverID) 



        return Response({
            'Successful message sent'
        })
