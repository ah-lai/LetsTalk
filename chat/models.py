from django.db import models
from django.contrib.auth.models import User


class message_sender(models.Model):
    user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT,primary_key=True)


class message_reciever(models.Model):
    user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT,primary_key=True)


class message(models.Model):
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)
    senderID = models.ForeignKey(message_sender,on_delete=models.PROTECT,related_name='senderID')
    recieverID = models.ForeignKey(message_reciever, on_delete=models.PROTECT,related_name='recieverID')



    
