from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field
from django import forms
from .models import Car, Reservation, PrivateMsg


class CarForm(forms.ModelForm):
    image = forms.ImageField()
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
            "stock",
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
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['car'].widget.attrs['style'] = 'pointer-events: None'
        self.fields['pickUpLocation'].widget.attrs['readonly'] = True
        self.fields['returnLocation'].widget.attrs['readonly'] = True
        self.fields['pickUpDate'].widget.attrs['readonly'] = True
        self.fields['returnDate'].widget.attrs['readonly'] = True

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
