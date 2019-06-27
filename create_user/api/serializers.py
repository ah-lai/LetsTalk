from rest_framework import serializers
from create_user.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user_id','first_name','last_name',
                  'email', 'phone_number', 'location',
                  'start_date')
