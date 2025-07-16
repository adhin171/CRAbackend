from rest_framework import serializers
from .models import Car,Rental,Purchase


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'