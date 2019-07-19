from rest_framework import serializers
from .models import message, message_reciever, message_sender

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ('content')


class SenderSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = message_sender
        fields = ('message')


class RecieverSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True, read_only=True)
    # I think this will make it have content in this object (switch to primary key)

    class Meta:
        model = message_reciever
        fields = ('message')
        
 # field may be wrong   
   
