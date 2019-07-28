from .api import MessageManager  
from django.urls import path, include

urlpatterns = [
    path("sendmessage/", MessageManager.as_view()),
]