from django.contrib import admin
from bookings.models import Bookings, BookingPayment

admin.site.register(Bookings)
admin.site.register(BookingPayment)