from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    sale_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    is_for_rent = models.BooleanField(default=True)
    is_for_sale = models.BooleanField(default=False)
    image = models.ImageField(upload_to='cars/',null=True,blank=True)
    status = models.CharField(max_length=20, default='available')

    def __str__(self):
        return f"{self.title} ({self.brand})"
    
class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    car = models.ForeignKey('car',on_delete=models.CASCADE,related_name='rentals')
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} → {self.car.title} ({self.start_date} to {self.end_date})"
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='purchases')
    sale_price = models.DecimalField(max_digits=10,decimal_places=2)
    purchased_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} bought {self.car.title} on {self.purchased_on.date()}"