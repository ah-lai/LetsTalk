from .api import  User_manager, LoginAPI, UserAPI, register_view
from django.urls import path, include

urlpatterns = [
    path("user/", User_manager.as_view()),
    path("login/", LoginAPI.as_view()),
    path("register/", register_view)
]