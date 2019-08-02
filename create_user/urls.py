from .api import  User_manager
from django.urls import path, include

urlpatterns = [
    path("user/", User_manager.as_view()),
]