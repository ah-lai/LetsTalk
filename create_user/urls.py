from .api import  RegistrationAPI, LoginAPI, UserAPI
from django.urls import path, include

urlpatterns = [
    path("registration/", RegistrationAPI.as_view()),
    path("login/", LoginAPI.as_view()),
]