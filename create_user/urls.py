from .api import  User_manager, LoginAPI, UserAPI
from django.urls import path, include

urlpatterns = [
    path("user/", User_manager.as_view()),
    path("login/", LoginAPI.as_view()),
]