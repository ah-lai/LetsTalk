from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from uuid import uuid4

class User(models.Model):
    user_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    location = models.CharField(max_length=45)  
    email = models.CharField(unique=True, max_length=100)  
    phone_num = models.CharField(unique=True, max_length=15)  
    start_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField( max_length=15)
    is_active = models.BooleanField(null=False, default=1)  

    object = models.Manager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    # must hash the password


    
    class Meta:
        managed = False
        db_table = 'user'

