from django.db import models

# Create your models here.
class Menu(models.Model):
    ID=models.IntegerField(primary_key=True),
    Title = models.CharField(max_length=255),
    Price = models.DecimalField(max_digits=10, decimal_places=2),
    Inventory = models.IntegerField()
    
       
def __str__(self):
    return self.Title
     
class Booking(models.Model):
    ID = models.IntegerField(primary_key=2),
    Name = models.CharField(max_length=255),
    No_of_guest = models.IntegerField(),
    BookingDate = models.DateTimeField()
    
def __str__(self):
    return self.Name

    

