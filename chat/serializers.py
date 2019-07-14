from rest_framework import serializers
from .models import message, message_reciever, message_sender

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ('message_id','content')



class SenderSerializer(serializers.ModelSerializer):
    message_id = serializers.StringRelatedField(many=False)
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = message_sender
        fields = ('user_id', 'message_id')


class RecieverSerializer(serializers.ModelSerializer):
    message_id = serializers.StringRelatedField(many=False)
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = message_reciever
        fields = ('user_id','message_id')