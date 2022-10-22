import django_filters
from .models import *


class HouseFilter(django_filters.FilterSet):
    class Meta:
        model = House
        fields = ['no_of_rooms', 'location', 'type_of_house', 'rent_price']
