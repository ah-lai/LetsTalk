from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model


class message(models.Model):
    message_id=models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid4())
    #generate a UUID for the message id
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)

    class meta:
        managed=False
        db_table='message'


class message_sender(models.Model):
    message_id = models.ForeignKey(message, db_column="message_id", on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT)

    class meta:
        managed=False
        db_table='message_sender'

class message_reciever(models.Model):
    message_id = models.ForeignKey(message, db_column="message_id", on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, db_column="user_id",on_delete=models.PROTECT)

    class meta:
        managed=False
        db_table='message_reciever'
    
