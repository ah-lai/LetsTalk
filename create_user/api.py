from django.http.response import JsonResponse
from rest_framework.views import APIView

from django.contrib.auth.models import User

from .serializers import UserSerializer


class User_manager(APIView):        
    # this doesn't work, request is nothing even if there is key+values
    def get(self,request, format=None):
        
        user_id = request.POST.get('id')

        #Get One User   
        if user_id:
            users = User.objects.filter(id=user_id)
        #Get all Users
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)