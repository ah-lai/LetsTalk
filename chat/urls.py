from .api import MessageManager, getMessage
from django.urls import path, include

urlpatterns = [
    path("sendmessage/", MessageManager.as_view()),
    path("getmessage/", getMessage.as_view()),
]