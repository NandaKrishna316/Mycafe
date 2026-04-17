from django.db import models
from django.contrib.auth.models import AbstractUser
   

class register(AbstractUser):
    username=models.CharField(max_length=100, unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    home_address = models.TextField(max_length=255)
    contact_number = models.CharField(max_length=15)


    def __str__(self):
        return self.email

class Tastes(models.Model):
    tastes = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tastes

class Complaint(models.Model):
    complaint_text = models.TextField(max_length=1050)

    def __str__(self):
        return self.complaint_text
