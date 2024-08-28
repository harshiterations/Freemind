from django.db import models
from django.contrib.auth.models import User
from therapist.models import Therapist
from availability.models import Slot
from bookings.constants import PaymentStatus



class Bookings(models.Model):
    Booking_status = [
        ('UPCOMING', 'Upcoming'),
        ('ACTIVE', 'Active'),
        ('PAST', 'Past')
    ]
    therapist = models.ForeignKey(Therapist,on_delete=models.CASCADE)
    meet_link = models.URLField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    client_name = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    status = models.CharField(choices=Booking_status, max_length=70,null=True)
    booking_notes = models.TextField(null=True)

    def __str__(self):
        return str(self.id)
    

class BookingPayment(models.Model):
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    provider_order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    signature_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=PaymentStatus, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)




