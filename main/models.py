from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class College (models.Model):
    name = models.CharField(max_length = 50)
    adress = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 10)

    def __str__(self):
        return self.name


class Subject (models.Model):

    AREA_GROUP = (
        ('CB', 'CIENCIAS BASICAS Y AMBIENTALES'),
        ('SA', 'CIENCIAS DE LA SALUD'),
        ('SH', 'CIENCIAS SOCIALES Y HUMANIDADES'),
        ('NG', 'ECONOMIA Y NEGOCIOS'),
        ('IN', 'INGENIERIAS'),
        )

    name = models.CharField(max_length = 50)
    area = models.CharField(max_length = 2, choices = AREA_GROUP)

    def __str__(self):
        return self.name

class User (AbstractUser):
    is_student = models.BooleanField(default = False)
    is_teacher = models.BooleanField(default = False)

    def __str__(self):
        return '%s, %s' % ( self.first_name, self.last_name)


class Student (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    college_id = models.ForeignKey(College, null = True, on_delete = models.SET_NULL)

class Tutor (models.Model):
    DEGREE_LEVEL = (
        ('EP', 'EDUCACION PRIMARIA'),
        ('ES', 'EDUCACION SECUNDARIA'),
        ('BA', 'BACHILLER'),
        ('GR', 'GRADO'),
        ('PG', 'POST-GRADO'),
        )


    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    degree = models.CharField(max_length = 2,choices = DEGREE_LEVEL)
    identity_document = models.CharField(max_length = 11)
    description = models.CharField(max_length = 100)
    subjects = models.ManyToManyField(Subject, related_name='Subjects')  

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Tutor.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.tutor.save()

class User_Request (models.Model):
     
    REQUEST_STATUS = (
        ('A', 'Accepted'),
        ('R', 'Rejected'),
        ('C', 'Cancelled'),
        ('P', 'Pending'),
        )

    student_ID = models.ForeignKey(Student, on_delete = models.CASCADE)
    tutor_ID = models.ForeignKey(Tutor,  on_delete = models.CASCADE)
    status = models.CharField(max_length = 1, choices = REQUEST_STATUS, blank = True, default = 'P')
    request_date = models.DateTimeField("Request date", default = datetime.now())

    


