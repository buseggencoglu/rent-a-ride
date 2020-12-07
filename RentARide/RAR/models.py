from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms

# Create your models here.


def uploaded_location(instance, filename):
    return ("%s/%s") % (instance.carName, filename)


class Car(models.Model):
    image = models.ImageField(upload_to=uploaded_location, null=True, blank=True, width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    carName = models.CharField(max_length=100,default="")
    userID = models.IntegerField()
    model = models.CharField(max_length=100)

    NUM_OF_SEATS_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    numOfSeats = models.IntegerField(
        choices=NUM_OF_SEATS_CHOICE,
    )

    numOfDoors = models.IntegerField(
        choices=NUM_OF_SEATS_CHOICE,
    )

    Manual = 'M'
    Automatic = 'A'
    CVT = 'C'

    TRANSMISSION_CHOICES = [
        (Manual, 'Manual'),
        (Automatic, 'Automatic'),
        (CVT, 'CVT'),
    ]
    transmission = models.CharField(
        max_length=1,
        choices=TRANSMISSION_CHOICES,
        default=Manual,
    )

    airconditioner = models.BooleanField()
    price = models.IntegerField()

    CAR_STATUS_CHOICES = [
        (1, 'Available'),
        (0, 'UnAvailable'),
    ]
    carStatus = models.IntegerField(
        choices=CAR_STATUS_CHOICES,
        default=1,
    )

    branchId = models.IntegerField()

    def __str__(self):
        return self.carName

    def get_absolute_url(self):
        return "/car/%s/" % (self.pk)


class Reservation(models.Model):
    carID = models.IntegerField()
    customerID = models.IntegerField()
    carDealerID = models.IntegerField()
    pickUpLocation = models.TextField()
    returnLocation = models.TextField()
    pickUpDate = models.DateTimeField()
    returnDate = models.DateTimeField()
    paymentStatus = models.BooleanField()

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.pk)


class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
