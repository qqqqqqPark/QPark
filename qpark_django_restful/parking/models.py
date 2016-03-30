from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='user_profile')

    #evaluation scores for users
    evaluation = models.FloatField(default = 0.0, blank = True)
    #how many times the user is evaluated
    evalNum = models.IntegerField(default = 0, blank = True)


class ParkingSpot(models.Model):
    owner = models.ForeignKey('auth.User', related_name='park_spot')
    availability = models.BooleanField(default=False)
    
    carPlateNo = models.CharField('Car plate No',max_length=10)
    
    
    state = models.CharField('State' , max_length = 30)
    city = models.CharField('City', max_length = 30)
    street = models.CharField('Street' , max_length = 30)
    houseNo = models.CharField('House #', max_length = 30)
    zipCode = models.CharField('Zip Code' , max_length = 10)

    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    
    
    #longitude
    lon = models.FloatField()
    #lattitude
    lat = models.FloatField()

    def __str__(self):
        return "Parking Spot " + str(self.pk)
    
    def getAddress(self):
        address = ""
        address += self.houseNo + " " + self.street + " " + \
                   self.city + " " + self.state + " " + str(self.zipCode)
        return address

class CarInfo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='car_info')

    parkId = models.IntegerField(default=-1)
    
    plateNo = models.CharField("Plate Number", max_length = 10)
    color = models.CharField("Color" , max_length = 20)

    length = models.FloatField();
    width = models.FloatField();
    height = models.FloatField();


    
