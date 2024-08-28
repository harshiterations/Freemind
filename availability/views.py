from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from availability.serailizers import Availabilityserailiser, Slotserializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from availability.models import Availability, Slot
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status

class Createavailabilityview(CreateAPIView):
    serializer_class = Availabilityserailiser
    permission_classes = [AllowAny]

class ListavailabilityView(ListAPIView):
    serializer_class = Availabilityserailiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        therapist_id = self.kwargs.get('therapist_id')
        return Availability.objects.filter(therapist=therapist_id)


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = Availabilityserailiser
    permission_classes = [IsAuthenticated]
    queryset = Availability.objects.all()


class FetchSlotsView(ListAPIView):
    serializer_class = Slotserializer
    def get_queryset(self):
        date = self.request.query_params.get('date')
        therapist_id = self.request.query_params.get('therapist')
        Date = datetime.strptime(date,'%Y-%m-%d')

        slots = Slot.objects.filter(
            availability__date=Date,
            availability__therapist=therapist_id,
            is_booked=False
        )

        if not slots.exists():
            day_of_the_week = Date.strftime('%A')
            slots = Slot.objects.filter(
                availability__day_of_week=day_of_the_week,
                availability__therapist=therapist_id,
                is_booked=False
            )

        return slots


