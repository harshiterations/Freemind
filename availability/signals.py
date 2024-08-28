from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Availability


@receiver(post_save, sender=Availability)
def create_slots_from_availability(sender, instance, created, **kwargs):
    if created:
        print("Life is enjoy")
        instance.create_slots()
