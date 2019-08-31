from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class College (models.Model):
    name = models.CharField(max_length = 100)
    adress = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 10)


# class Student (models.Model):
#     name = models.CharField(max_length = 100)
#     email = models.CharField(max_length = 100)
#     password = 


class User_Request (models.Model):

     student_ID = models.ForeignKey(User, default = 1, on_delete = models.SET_DEFAULT)
     #tutor_id = models.ForeignKey(,default = 0, on_delete = models.SET_DEFAULT)
     status = models.IntegerField()
     request_date = models.DateTimeField("Request date", default = datetime.now())


class Subject (models.Model):

    name = models.CharField(max_length = 50)
    area = models.CharField(max_length = 50)