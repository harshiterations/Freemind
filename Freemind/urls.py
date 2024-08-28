# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('availability/', include('availability.urls')),
    path('therapist/', include('therapist.urls')),
    path('bookings/', include('bookings.urls'))

]

