from .api import UserAPI  
from django.urls import path, include

urlpatterns = [
    path("user/", UserAPI.as_view()),
]