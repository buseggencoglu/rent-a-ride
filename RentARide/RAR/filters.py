from .models import Car
import django_filters
from .models import models
from .forms import forms


class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            'model': ['exact'],
            'numOfDoors': ['exact'],
            'numOfSeats': ['exact'],
            'transmission': ['exact'],
            'airconditioner': ['exact'],
            'price': ['exact', 'lt', 'gt'],
            'branch': ['exact'],
        }
        filter_overrides = {
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
        }