from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.

class College (models.Model):
    name = models.CharField(max_length = 50)
    adress = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 10)

    def __str__(self):
        return self.name


class Subject (models.Model):
    name = models.CharField(max_length = 50)
    area = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class User (AbstractUser):
    is_student = models.BooleanField(default = False)
    is_teacher = models.BooleanField(default = False)

    def __str__(self):
        return '%s, %s' % ( self.first_name, self.last_name)


class Student (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default = 1, primary_key = True)
    college_id = models.ForeignKey(College, null = True, on_delete = models.SET_NULL)

class TutorH (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default = 2, primary_key = True)
    degree = models.CharField(max_length = 50)
    identity_document = models.CharField(max_length = 11)
    description = models.CharField(max_length = 100)

class TutorD (models.Model):
    tutorH_ID = models.OneToOneField(TutorH, null = True, on_delete = models.CASCADE)
    subject_ID = models.ForeignKey(Subject, null = True, on_delete = models.SET_NULL)   


class User_Request (models.Model):
     
    REQUEST_STATUS = (
        ('A', 'Accepted'),
        ('R', 'Rejected'),
        ('C', 'Cancelled'),
        ('P', 'Pending'),
        )

    student_ID = models.ForeignKey(Student, on_delete = models.CASCADE)
    tutor_ID = models.ForeignKey(TutorH,  on_delete = models.CASCADE)
    status = models.CharField(max_length = 1, choices = REQUEST_STATUS, blank = True, default = 'P')
    request_date = models.DateTimeField("Request date", default = datetime.now())

    


