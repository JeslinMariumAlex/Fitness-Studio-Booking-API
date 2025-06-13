from rest_framework import serializers
from django.utils.timezone import localtime
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'
        
    def get_datetime(self, obj):
        # Convert UTC datetime to IST
        return localtime(obj.datetime).isoformat()

    

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'