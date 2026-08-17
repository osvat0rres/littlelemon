from django.db import models
from datetime import datetime


# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    BookingData = models.DateTimeField()
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    Tittle = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(5)
    
    def __str__(self):
        return self.Tittle
    
    
    
