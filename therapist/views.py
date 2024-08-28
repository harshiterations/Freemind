from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from therapist.serializers import Therapistdetailserilizer
from therapist.models import Therapist
from rest_framework.permissions import IsAuthenticated, AllowAny
from therapist.filters import TherapistFilter
from rest_framework import pagination


class CreateTherapistView(CreateAPIView):
    serializer_class = Therapistdetailserilizer
    queryset = Therapist.objects.all()
    permission_classes = [AllowAny]


class ListTherapistView(ListAPIView):
    serializer_class = Therapistdetailserilizer
    permission_classes = [AllowAny]
    queryset = Therapist.objects.all()
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 1
    filterset_class = TherapistFilter


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = Therapistdetailserilizer
    queryset = Therapist.objects.all()
    permission_classes = [AllowAny]


