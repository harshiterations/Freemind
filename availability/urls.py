from django.urls import path
from .views import Createavailabilityview, FetchSlotsView


urlpatterns = [
    path('create/', Createavailabilityview.as_view(), name='index'),
    path('slots/', FetchSlotsView.as_view(), name='slots')
]
