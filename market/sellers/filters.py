from django_filters import rest_framework
from market.sellers.models import Factory


class CountryFilter(rest_framework.FilterSet):
    class Meta:
        model = Factory
        fields = ("country",)
