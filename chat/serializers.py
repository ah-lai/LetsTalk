from rest_framework import serializers
from .models import  message_reciever, message_sender



class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = message_sender
        fields = ['content']    



class RecieverSerializer(serializers.ModelSerializer):
    class Meta:
        model = message_reciever
        fields = ['content']
        