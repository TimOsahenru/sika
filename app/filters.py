import django_filters
from .models import *


class HouseFilter(django_filters.FilterSet):
    class Meta:
        model = House
        fields = ['area', 'house_type', 'price']

