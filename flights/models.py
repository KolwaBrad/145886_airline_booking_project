# flights/models.py
from django.db import models
from django.core.validators import MinLengthValidator

class Flight(models.Model):
    flight_number = models.CharField(
        max_length=10, 
        unique=True, 
        validators=[MinLengthValidator(3)]
    )
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    flight = models.ForeignKey(
        Flight, 
        on_delete=models.CASCADE, 
        related_name='passengers'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"