from django.db import models
from signup.models import Signup

class ParkingLocation(models.Model):
    LocationName=models.CharField(max_length=100)
    def __str__(self):
        return str(self.LocationName) 
    class Meta:
        db_table="parkinglocation"


class ParkingInfo(models.Model):
    ParkingName=models.CharField(max_length=100)
    OwnerName=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    ContactNo=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    ParkingFee=models.IntegerField(max_length=10)
    Status=models.CharField(max_length=100)
    LocationID = models.ForeignKey(ParkingLocation, on_delete = models.SET_NULL,null =True)

    def __str__(self):
        return str(self.ParkingName) + " " + str(self.OwnerName) + " " + str(self.ParkingFee) 
    class Meta:
        db_table="parkinginfo"

class ParkingSpace(models.Model):
    ParkingID = models.ForeignKey(ParkingInfo, on_delete = models.SET_NULL,null =True)
    SpaceName=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Status=models.CharField(max_length=100,null=True,default='Available')
    def __str__(self):
        return str(self.SpaceName) + " "  + str(self.Description) 
    
    class Meta:
        db_table="parkingspace"

class BookSpace(models.Model):
    SpaceID = models.ForeignKey(ParkingSpace, on_delete = models.SET_NULL,null =True)
    BookDate=models.CharField(max_length=100)
    BookTime=models.CharField(max_length=100)
    PaymentMode=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    CardHolderName=models.CharField(max_length=100)
    CardNo=models.CharField(max_length=100) 
    CVV=models.CharField(max_length=100) 
    Status=models.CharField(max_length=100)
    bookedby = models.ForeignKey(Signup, on_delete = models.SET_NULL,null =True)
    
    class Meta:
        db_table="bookspace"