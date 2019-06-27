from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    location = models.CharField(db_column='Location', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', unique=True, max_length=15)  # Field name made lowercase.
    start_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'user'