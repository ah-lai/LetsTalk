from create_user.models import User
from create_user.api.serializers import UserSerializer
from rest_framework import generics


class UserlistCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer