from django.db import models

# Create your models here.

class User_Detail(models.Model):
    user_id=models.CharField(max_length=20)
    user_name=models.CharField(max_length=100)
    tz=models.CharField(max_length=50)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()


# input_formats='%m,%d,%Y %H:%M%p'    