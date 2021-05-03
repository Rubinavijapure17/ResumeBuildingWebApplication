from django.db import models
from django.urls import reverse
# Create your models here.

class Resume(models.Model):
    Name=models.CharField(max_length=30)
    Address=models.TextField(   )
    Phone_No=models.IntegerField()
    Emailid=models.CharField(max_length=30)
    SSC=models.CharField(max_length=30)
    HSC=models.CharField(max_length=30)
    UG=models.CharField(max_length=30)
    PG=models.CharField(max_length=30)
    Skills=models.TextField()
    Languages=models.TextField()
    Certificates=models.TextField()
    Projects=models.TextField()
    Experience=models.TextField()
    Summary=models.TextField()

    def get_absolute_url(self):
        return reverse('list')