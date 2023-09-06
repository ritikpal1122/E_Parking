from django.db import models

class Signup(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    ContactNo=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    class Meta:
        db_table="signup"
