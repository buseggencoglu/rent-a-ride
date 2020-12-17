from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms


# Create your models here.


def uploaded_location(instance, filename):
    return ("%s/%s") % (instance.carName, filename)


class Branch(models.Model):
    branch_name = models.CharField(max_length=100, default="")
    branch_location = models.TextField()

    def __str__(self):
        return self.branch_name


class Car(models.Model):
    image = models.ImageField(upload_to=uploaded_location, null=True, blank=True, width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    carName = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100)
    airconditioner = models.BooleanField()
    price = models.IntegerField()
    branchId = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    stock = models.IntegerField(default=0)

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

    CAR_STATUS_CHOICES = [
        (1, 'Available'),
        (0, 'UnAvailable'),
    ]
    carStatus = models.IntegerField(
        choices=CAR_STATUS_CHOICES,
        default=1,
    )

    class Meta:
        db_table = 'car'

    def __str__(self):
        return f'{self.carName}-{self.model}'

    def get_absolute_url(self):
        return "/car/%s/" % (self.pk)

    @classmethod
    def view_car_list(cls):
        return cls.objects.values('id', 'model', 'carStatus')

    @classmethod
    def view_car_detail(cls, car_id):
        return cls.objects.get(id=car_id)

    @classmethod
    def search_for_car(cls, busy_cars, branch_id):
        return cls.objects.filter(branchId=branch_id).exclude(busy_cars)


class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()


# natika was here .d

class User(models.Model):
    username = models.CharField(max_length=100, default='', unique=True)
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=32)  # login formda pswrd input gir.
    email = models.EmailField()

    def __str__(self):
        return self.name

    @classmethod
    def view_users(cls):
        return cls.objects.values('id', 'name', 'lastname')


class Admin(User):
    pass

    def __str__(self):
        return self.name


class Reservation(models.Model):
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
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

    # carID__model yerine carID olması gerekmiyor mu
    @classmethod
    def view_users_history(cls, customerID):
        return cls.objects.filter(customerID=customerID).values('carID__model', 'pickUpDate', 'returnDate',
                                                                'pickUpLocation', 'returnLocation',
                                                                'customerID__name', 'customerID__lastname')

    @classmethod
    def used_cars(cls, pickup_date, return_date):
        return cls.objects.filter(pickUpDate__gte=pickup_date, returnDate__lte=return_date).values('carID__id')


# -----------------CarDealer Section-----------------#


class CarDealer(User):
    branchId = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)
    rate = models.IntegerField(null=True)

    def __str__(self):
        return self.name
