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

    # get for messages
    def get(self, request, format=None):

        sender = request.POST.get('sender')
        reciever = request.POST.get('reciever')

        unread_messages = message.objects.filter(sender=sender, reciever=reciever, is_read=False)
        serializer = MessageSerializer(unread_messages, many=True, context={'request': request})

        for messages in unread_messages:
            messages.is_read = True
            messages.save()

        return JsonResponse(serializer.data,safe=False)

    