from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.

class College (models.Model):
    name = models.CharField(max_length = 50)
    adress = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 10)


class Subject (models.Model):
    name = models.CharField(max_length = 50)
    area = models.CharField(max_length = 50)

class Student (AbstractUser):
    college_id = models.ForeignKey(College, on_delete = models.SET_NULL)

class TutorH (AbstractUser):
    degree = models.CharField(max_length = 50)
    identity_document = models.CharField(max_length = 11)
    description = models.CharField(max_length = 100)

class TutorD (models.Model):
    tutorH_ID = models.OneToOneField(TutorH, on_delete = models.CASCADE)
    subject_ID = models.ForeignKey(Subject, on_delete = models.SET_NULL)   


class User_Request (models.Model):

     student_ID = models.ForeignKey(Student, on_delete = models.SET_NULL)
     tutor_id = models.ForeignKey(TutorH, on_delete = models.SET_NULL)
     status = models.IntegerField()
     request_date = models.DateTimeField("Request date", default = datetime.now())


