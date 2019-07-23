from .api import SendMessageAPI  
from django.urls import path, include

urlpatterns = [
    path("sendmessage/", SendMessageAPI.as_view()),
]