from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field
from django import forms
from .models import Car, Reservation, PrivateMsg


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "image",
            "carName",
            "model",
            "numOfDoors",
            "numOfSeats",
            "transmission",
            "airconditioner",
            "price",
            "carStatus",
            "branch",
        ]


class ReservationSearchForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "pickUpLocation",
            "returnLocation",
            "pickUpDate",
            "returnDate",
        ]


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = [
            'car',
            'pickUpLocation',
            'returnLocation',
            'pickUpDate',
            'returnDate',
        ]



class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]
