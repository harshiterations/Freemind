from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from bookings.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from bookings.models import Bookings, BookingPayment
from bookings.constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import razorpay
from django.conf import settings
from rest_framework.response import Response



class CreatebookingsView(CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    queryset = Bookings.objects.all()

    def perform_create(self, serailizer):
        booking = serailizer.save()
        booking.slot.is_booked = True
        booking.slot.save()


    
class CreateBookingPaymentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        booking_id = request.data.get('booking_id')
        amount = (request.data.get('amount'))
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        razorpay_order = client.order.create({
            "amount": int(amount) * 100,
            "currency": "INR",
            "payment_capture": "1"
        })

        booking_payment = BookingPayment.objects.create(
            booking_id=booking_id,
            amount=amount,
            provider_order_id=razorpay_order['id']
        )

        return render(request, "payment.html", {
            "order_id": razorpay_order['id'],
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "amount": amount,
            "booking_payment_id": booking_payment.id
        })


@method_decorator(csrf_exempt, name='dispatch')
class RazorpayCallbackView(APIView):

    def post(self, request):
        def verify_signature(response_data):
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            return client.utility.verify_payment_signature(response_data)

        razorpay_order_id = request.data.get('razorpay_order_id')
        payment_id = request.data.get('razorpay_payment_id')
        signature = request.data.get('razorpay_signature')

        booking_payment = BookingPayment.objects.get(provider_order_id=razorpay_order_id)
        booking_payment.payment_id = payment_id
        booking_payment.signature_id = signature

        if verify_signature(request.data):
            booking_payment.status = 'SUCCESS'
            booking_payment.booking.is_paid = True
            booking_payment.booking.save()
        else:
            booking_payment.status = PaymentStatus.FAILURE

        booking_payment.save()

        return Response({"status": booking_payment.status})
