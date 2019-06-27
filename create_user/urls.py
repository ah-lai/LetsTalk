from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UserlistCreate.as_view() ),
]