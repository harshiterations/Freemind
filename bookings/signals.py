from django.db.models.signals import post_save
from django.dispatch import receiver
from bookings.models import Bookings
from googleapiclient.errors import HttpError
from createevent import create_event
from .tasks import create_event_in_calender



@receiver(post_save, sender=Bookings)
def create_calendar_event(sender, instance, created, **kwargs):
    print("Signal received for Booking:", instance.id, "Created:", created)
    if instance.is_paid and not instance.meet_link:
        print("This booking is paid")
        booking_id = instance.id
        print(booking_id)
        create_event_in_calender.delay(booking_id)
        print("I am mad") 