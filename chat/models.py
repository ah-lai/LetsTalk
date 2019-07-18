from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model


class messageSender(models.Model):
    user = models.ForeignKey(message_sender, related_name='message', on_delete=models.CASCADE)
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)
    
class messageReciever(models.Model):
    user = models.ForeignKey(message_reciever, related_name='message', on_delete=models.CASCADE)
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)


class message_sender(models.Model):
     user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT,primary_key=True)
     


class message_reciever(models.Model):
    user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT,primary_key=True)


    
