from django.urls import path
from therapist.views import CreateTherapistView, ListTherapistView, RetrieveUpdateDestroyView


urlpatterns = [
    path('create/', CreateTherapistView.as_view(), name='index'),
    path('', ListTherapistView.as_view(), name='TherapistList'),
    path('<int:pk', RetrieveUpdateDestroyView.as_view())
]