from rest_framework import serializers
from .models import message, message_reciever, message_sender

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ('content',)

class SenderSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = message_sender
        fields=('message',)


class RecieverSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = message_reciever
        fields=('message',)

        
        

