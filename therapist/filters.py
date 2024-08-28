import django_filters
from .models import Therapist, Category, Language


class TherapistFilter(django_filters.FilterSet):
    language = django_filters.CharFilter(
        label='Language',
        field_name = 'language__name'
    )

    experience = django_filters.NumberFilter(
        field_name='experience',
        lookup_expr='gte',
        label='Experience (years)'
    )

    session_fees = django_filters.RangeFilter(
        field_name='session_fees',
        label='Price Range'
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Category'
    )

    class Meta:
        model = Therapist
        fields = []