from django.contrib import admin
from therapist.models import Therapist, Category, Language, Testimonial

admin.site.register(Therapist)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Testimonial)