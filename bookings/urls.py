from django.urls import path
from bookings.views import CreatebookingsView, CreateBookingPaymentView, RazorpayCallbackView

urlpatterns = [
    path('create/', CreatebookingsView.as_view(), name='index'),
    path('initiate_payment/', CreateBookingPaymentView.as_view(), name='payment Initialization'),
    path('callback_payment/', RazorpayCallbackView.as_view(), name='payment callback')

]
