from rest_framework import serializers
from therapist.models import Therapist


class Therapistdetailserilizer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'
