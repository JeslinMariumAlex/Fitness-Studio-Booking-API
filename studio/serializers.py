from rest_framework import serializers
from django.utils.timezone import localtime
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'

    def get_datetime(self, obj):
        return localtime(obj.datetime).isoformat()

class BookingSerializer(serializers.ModelSerializer):
    fitness_class = FitnessClassSerializer(read_only=True)  # Nest full class details

    class Meta:
        model = Booking
        fields = '__all__'
