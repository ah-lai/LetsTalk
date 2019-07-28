from django.db import models
from django.contrib.auth.models import User


class message(models.Model):
    content=models.CharField(max_length=2000)
    send_time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender', null=False)
    reciever = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciever', null=False)
    is_read = models.BooleanField(default=False)

    class Meta:
        managed = True

    


    
