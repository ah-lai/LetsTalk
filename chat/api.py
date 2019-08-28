from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse

from create_user.serializers import  UserSerializer
from .serializers import MessageSerializer

from .models import message

class MessageManager(APIView):

    #Request will have the TOKEN(sender user_id), content, reciver user_id
    def post(self, request, *args, **kwargs):

        Message = MessageSerializer(data=request.data)
        Message.is_valid(raise_exception=True)
        Message.save()
        return JsonResponse(Message.data, status=201)

class getMessage(APIView):
    # get for messages
    def post(self, request, format=None):
        userID = request.data['userID']
        messages = message.objects.filter(reciever=userID)
        serializer = MessageSerializer(messages, many=True, context={'request': request})

        return JsonResponse(serializer.data,safe=False)
    