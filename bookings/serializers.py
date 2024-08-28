from rest_framework import serializers
from bookings.models import Bookings

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'