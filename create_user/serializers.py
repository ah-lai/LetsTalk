from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['fname','lname',
                  'email', 'phone_num', 'location',
                  'start_date', 'password']

        # Validate if it is a unique email 


class UserSerializer():
    class Meta:
        modal = User 
        fields = ('user_id','email')


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField() 

    def validate(self, data):
        print(data)
        user = authenticate(**data) #error occuring here 
        if user:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")