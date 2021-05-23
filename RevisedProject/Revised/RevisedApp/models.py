from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
	t=[('CSE','CSE'),('ECE','ECE'),('CIVIL','CIVIL'),('Mechanical','Mechanical'),('EEE','EEE'),('MBA','MBA')]
	y=[('III','III'),('IV','IV')]
	rollno=models.CharField(default='17AK1A000',max_length=10)
	dob=models.DateField(null=True)
	year=models.CharField(choices=y,max_length=5,null=True)
	dept=models.CharField(choices=t,max_length=12,null=True)
	phone_no=models.IntegerField(null=True)
	percentage=models.IntegerField(null=True)
	backlogs=models.IntegerField(null=True)
	pass_year=models.IntegerField(null=True)
	address=models.CharField(max_length=250,null=True)
	r=[(1,'coordinator'),(2,'Student'),(3,'Guest')]
	role=models.IntegerField(choices=r,default=3)



class Coordinator(models.Model):
	t=[('CSE','CSE'),('ECE','ECE'),('CIVIL','CIVIL'),('Mechanical','Mechanical'),('EEE','EEE'),('MBA','MBA')]
	cord_name=models.CharField(max_length=10,null=True)
	dept=models.CharField(choices=t,max_length=12,null=True)
	phone_no=models.IntegerField(null=True)


class Jobinfo(models.Model):
	title=models.CharField(max_length=25)
	location=models.CharField(max_length=20)
	salary=models.IntegerField(null=True)
	skills=models.CharField(max_length=30)
	job_role=models.CharField(max_length=30)
	eligible_percent=models.IntegerField(null=True)
	eligible_dept=models.CharField(max_length=30)
	year_of_pass=models.IntegerField(null=True)
	last_date=models.DateField(null=True)
	descrip=models.CharField(max_length=250)
	com_image=models.ImageField(upload_to='Jobs/',default='123.jpg')

