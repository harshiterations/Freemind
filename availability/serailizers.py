from rest_framework import serializers
from availability.models import Availability, Slot



class Availabilityserailiser(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'



class Slotserializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'