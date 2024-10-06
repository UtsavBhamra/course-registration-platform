from django.db import models
from accounts.models import Student,Faculty

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

class Course(models.Model):
    code = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100,null=True)
    requested_students = models.ManyToManyField(Student,related_name="req_students")
    accepted_students = models.ManyToManyField(Student,related_name="acc_students")
    instructors = models.ManyToManyField(Faculty)
    schedule = models.CharField(max_length=50)
    department = models.CharField(choices=DEPARTMENT_CHOICES,max_length=50)
    credits = models.IntegerField()

class Cart(models.Model):
    courses = models.ManyToManyField(Course,blank=True)
    student = models.OneToOneField(Student,on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
