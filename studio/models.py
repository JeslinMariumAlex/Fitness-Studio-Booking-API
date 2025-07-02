from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

# Create your models here.
class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()


    def __str__(self):
        local_dt = localtime(self.datetime)
        return f"{self.name} by {self.instructor} on {local_dt.strftime('%Y-%m-%d %I:%M %p')}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_name}  -  {self.fitness_class.name}"
