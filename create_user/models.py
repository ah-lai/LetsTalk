# from django.db import models
# from django.contrib.auth.models import User


# class UserInfo(models.Model):
#     user_id = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE, null=True)
#     fname = models.CharField(max_length=45)
#     lname = models.CharField(max_length=45)
#     location = models.CharField(max_length=45)  
#     phone_num = models.CharField(unique=True, max_length=15)  
#     start_date = models.DateTimeField(auto_now_add=True)
    
#     must hash the password
    
#     class Meta:
#        managed = True
#        db_table = 'user'

