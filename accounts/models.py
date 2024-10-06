from django.db import models
from django.contrib.auth.models import AbstractUser

DEPARTMENT_CHOICES = [
    ("CSE","Computer Science and Engineering"),
    ("IT","Information Technology"),
    ("ECE","Electronics and Communication Engineering"),
    ("EEE","Electronics and Electrical Engineering"),
    ("ME","Mechanical Engineering"),
    ("CH","Chemical Engineering"),
    ("CV","Civil Engineering"),
    ("MME","Mining and Metallurgical Engineering")
]

PROGRAM_CHOICES = [
    ("B.Tech","Bachelor of Technology"),
    ("M.Tech","Master of Technology"),
    ("Ph.D.","Doctor of Philosophy"),
    ("MBA","Masters of Business Administration"),
    ("MCA","Masters of Computer Application")
]

USER_CHOICES= [
    ("ST","Student"),
    ("FA","Faculty"),
    ("AD","Admin")
]

class CustomUser(AbstractUser):
    user_type = models.CharField(choices=USER_CHOICES,max_length=10)

class Student(models.Model):
    student_user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    department = models.CharField(choices=DEPARTMENT_CHOICES,max_length=50)
    program_type = models.CharField(choices=PROGRAM_CHOICES,max_length=50)
    student_id = models.IntegerField(unique=True)

class Faculty(models.Model):
    faculty_user = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    department = models.CharField(choices=DEPARTMENT_CHOICES,max_length=50)
    faculty_id = models.IntegerField(unique=True)

class Admin(models.Model):
    admin_user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)