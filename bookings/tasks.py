from celery import shared_task
from .models import Bookings
from createevent import create_event



@shared_task(name='create_event_in_calender',)
def create_event_in_calender(booking_id):
    print("the task is running")
    booking = Bookings.objects.get(id=booking_id)
    start_datetime = booking.slot.start_time
    end_datetime = booking.slot.end_time
    therapist_name = booking.therapist.display_name
        
    event_result = create_event(start_datetime, end_datetime, therapist_name)
        
    if event_result['status'] == 'success':
        booking.meet_link = event_result['meet_link']
        booking.save(update_fields=['meet_link'])
        booking.slot.is_booked = True
        booking.slot.save(update_fields=['is_booked'])
        print(f"Event created successfully. Meet link: {booking.meet_link}")
    else:
        print(f"Failed to create event: {event_result['message']}")
