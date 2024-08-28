from django.db.models.signals import post_save
from django.dispatch import receiver
from bookings.models import Bookings
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from createevent import create_event


@receiver(post_save, sender=Bookings)
def create_calendar_event(sender, instance, created, **kwargs):
    print("Signal received for Booking:", instance.id, "Created:", created)
    if instance.is_paid and not instance.meet_link:
        print("This booking is paid")
        start_datetime = instance.slot.start_time
        end_datetime = instance.slot.end_time
        therapist_name = instance.therapist.display_name
        
        event_result = create_event(start_datetime, end_datetime, therapist_name)
        
        if event_result['status'] == 'success':
            instance.meet_link = event_result['meet_link']
            instance.save(update_fields=['meet_link'])
            instance.slot.is_booked = True
            instance.slot.save(update_fields=['is_booked'])
            print(f"Event created successfully. Meet link: {instance.meet_link}")
        else:
            print(f"Failed to create event: {event_result['message']}")