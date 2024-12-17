# flights/serializers.py
from rest_framework import serializers
from .models import Flight, Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'flight']

class FlightSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True, read_only=True)
    available_seats = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = [
            'id', 
            'flight_number', 
            'departure', 
            'arrival', 
            'origin', 
            'destination', 
            'capacity', 
            'passengers', 
            'available_seats'
        ]

    def get_available_seats(self, obj):
        return obj.capacity - obj.passengers.count()