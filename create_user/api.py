from rest_framework import viewsets, permissions, generics
from django.http.response import JsonResponse, HttpResponse
from rest_framework.views import APIView

from django.contrib.auth.models import User

from django.contrib.auth import login

from knox.models import AuthToken
from knox.auth import TokenAuthentication

from .serializers import  CreateUserSerializer, LoginUserSerializer, UserSerializer


class User_manager(APIView):

    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        _, token = AuthToken.objects.create(user)
        return JsonResponse({
            "user": UserSerializer(user).data,
            "token": token
        })

    def get(self,request, format=None):
        
        pk = request.GET.get('id')

        print(pk)

        #Get One User   
        if pk:
            users = User.objects.filter(id=pk)
        #Get all Users
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

   
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        login(request,user)
        
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user