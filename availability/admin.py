from django.contrib import admin
from availability.models import Availability, Slot


admin.site.register(Availability)
admin.site.register(Slot)
