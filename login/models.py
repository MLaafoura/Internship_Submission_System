from django.db import models    
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    is_careercenter = models.BooleanField(default=False)



    
class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='coordinator')
    FullName = models.CharField(max_length=100)
    def __str__(self):
        return self.FullName
    class Meta:
        db_table="login_coordinator"
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
    FullName = models.CharField(max_length=100)
    Field = models.CharField(max_length=50)
    level = models.CharField(max_length=20)
    coordinator = models.ForeignKey(Coordinator , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.FullName
      
class CareerCenter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='careercenter')

