from django.db import models
from django.contrib.auth.models import User


class message_sender(models.Model):
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)
    senderID = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT)

class message_reciever(models.Model):
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)
    recieverID = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT)


