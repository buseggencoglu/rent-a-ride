from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

class Branch(models.Model):
    branch_name = models.CharField(max_length=100, default="")
    branch_location = models.TextField()

    @classmethod
    def get_by_branch_name(cls, branch_name):
        return cls.objects.filter(branch_name__contains=branch_name)

    def __str__(self):
        return self.branch_name


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# -----------------CarDealer Section-----------------#

class CarDealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branchId = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)
    rate = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username


# -----------------Customer Section------------------#

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    licenseId = models.CharField(max_length=20, null=True)

    @classmethod
    def get_customer_by_user(cls, user):
        return cls.objects.filter(user=user)[0]


class Car(models.Model):
    image = models.ImageField(upload_to='car_image', null=True, blank=True, default='car_image/default')
    carName = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100)
    airconditioner = models.BooleanField()
    price = models.IntegerField()
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)

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
    def search_for_car(cls, busy_cars, branch_name):
        return cls.objects\
            .filter(branch__branch_name=branch_name)\
            .exclude(id__in=busy_cars)


class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()


class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    carDealer = models.ForeignKey(CarDealer, null=True, on_delete=models.CASCADE)
    pickUpLocation = models.CharField(max_length=100)
    returnLocation = models.CharField(max_length=100)
    pickUpDate = models.DateTimeField()
    returnDate = models.DateTimeField()
    paymentStatus = models.BooleanField(default=False)  # default false konulmalı
    total_price = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.pk)

    @classmethod
    def view_users_history(cls, customerID):
        return cls.objects.filter(customerID=customerID).values('carID__model', 'pickUpDate', 'returnDate',
                                                                'pickUpLocation', 'returnLocation',
                                                                'customerID__name', 'customerID__lastname')

    @classmethod
    def busy_cars(cls, start_date_date, end_date_date):
        return cls.objects.filter(Q(pickUpDate__date__range=[start_date_date, end_date_date]) |
                                  Q(pickUpDate__date__lte=start_date_date,
                                    returnDate__date__gte=end_date_date))\
                          .values('car__id')




class CarDealerCustomerSystem():
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    # user_name = models.CharField(max_length=100, blank=True)
    # user_lastname = models.CharField(max_length=100, blank=True)
    # mail = models.EmailField(max_length=150)
    # signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
