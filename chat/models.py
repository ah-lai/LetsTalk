from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model


class message(models.Model):
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)


class message_sender(models.Model):
    user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT,primary_key=True)
    #message_id = models.ForeignKey(User, db_column="id",on_delete=models.PROTECT)


class message_reciever(models.Model):
    user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT,primary_key=True)
    #message_id = models.ForeignKey(User, db_column="id",on_delete=models.PROTECT)


    
