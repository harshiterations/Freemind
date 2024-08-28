from datetime import timedelta, datetime
from django.db import models
from therapist.models import Therapist

class Availability(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=[
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ])
    date = models.DateField(blank=True)

    def create_slots(self):
        slots = []
        current_start_time = datetime.combine(datetime.today(), self.start_time)
        slot_duration = int(self.therapist.slot_duration)
        slot_duration = timedelta(minutes=slot_duration)
        end_time = datetime.combine(datetime.today(), self.end_time)

        while current_start_time + slot_duration <= end_time:
            slot = Slot(
                start_time=current_start_time,
                end_time=current_start_time + slot_duration,
                availability=self,
            )
            slots.append(slot)
            current_start_time += slot_duration

        if slots is not None:
            Slot.objects.bulk_create(slots)
            print(current_start_time)
        else:
            print("this sucks")


class Slot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)



