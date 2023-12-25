from django.db import models

# Create your models here.
class Students(models.Model):
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

class Admin(models.Model):
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)

class Lecturers(models.Model):
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

class Courses(models.Model):
    cname=models.CharField(max_length=30)
    level=models.CharField(max_length=10)

class Booked(models.Model):
    smail=models.CharField(max_length=20)
    cname=models.CharField(max_length=20)
    level=models.CharField(max_length=20)
    date=models.CharField(max_length=20)