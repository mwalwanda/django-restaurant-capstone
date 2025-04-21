from django.db import models

# Create your models here.
class Menu(models.Model):
    #ID=models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inventory = models.IntegerField(default=0)
           
    def __str__(self):
         return f'{self.title} : {str(self.price)}'
     
class Booking(models.Model):
    #id = models.IntegerField(primary_key=2)
    name = models.CharField(max_length=100, blank=True)
    no_of_guest = models.IntegerField(default=0)
    bookingDate = models.DateField(null=True)
    
    def __str__(self):
        return self.name

    

