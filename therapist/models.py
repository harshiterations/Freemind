from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    categories_image = models.ImageField(upload_to='categories/', blank=False, null=False)
    display_name = models.CharField(max_length=40,)

    def __str__(self):
        return self.display_name

class Testimonial(models.Model):
    auther_name = models.CharField(max_length=50)
    testimonial_content = models.TextField()

    def __str__(self):
        return self.auther_name

class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Therapist(models.Model):
    display_name = models.CharField(max_length=50)
    about = models.TextField()
    is_available_offline = models.BooleanField(default=False)
    happy_sessions = models.IntegerField(default=453)
    slot_duration = models.IntegerField(default=30)
    categories = models.ManyToManyField(Category)
    session_fees = models.DecimalField(decimal_places=2,max_digits=6)
    address = models.CharField(max_length=120, blank=True)
    profile_picture = models.ImageField(upload_to='therapists/', blank=True, null=True)
    educational_qualification = models.CharField(max_length=60)
    language = models.ManyToManyField(Language)
    testimonial = models.ManyToManyField(Testimonial)

    def __str__(self):
        return f"{self.display_name} {self.id}"













