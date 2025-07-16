from django.contrib import admin
from .models import Car
from .models import Rental
from .models import Purchase

# Register your models here.

admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(Purchase)