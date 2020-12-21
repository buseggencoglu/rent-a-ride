from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Car, Reservation, PrivateMsg, CarDealer
from .forms import CarForm, ReservationForm, MessageForm


def home(request):
    context = {
        "title": "Car Rental"
    }
    return render(request, 'home.html', context)


def car_list(request):
    car = Car.objects.all()

    query = request.GET.get('q')
    if query:
        car = car.filter(
            Q(carName__icontains=query) |
            Q(model__icontains=query) |
            Q(numOfSeats__icontains=query) |
            Q(numOfDoors__icontains=query)|
            Q(transmission=query) |
            Q(airconditioner__icontains=query) |
            Q(price__icontains=query) |
            Q(carStatus__icontains=query)
        )

    # pagination
    paginator = Paginator(car, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        car = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car = paginator.page(paginator.num_pages)
    context = {
        'car': car,
    }
    return render(request, 'car_list.html', context)


def car_detail(request, id=None):
    detail = get_object_or_404(Car, id=id)
    context = {
        "detail": detail
    }
    return render(request, 'car_detail.html', context)


@login_required
def car_created(request):
    form = CarForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/")
    context = {
        "form": form,
        "title": "Create Car"
    }
    return render(request, 'car_create.html', context)


@login_required()
def car_update(request, id=None):
    detail = get_object_or_404(Car, id=id)
    form = CarForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update Car"
    }
    return render(request, 'car_create.html', context)


@login_required()
def car_delete(request, id=None):
    query = get_object_or_404(Car, id=id)
    query.delete()

    car = Car.objects.all()
    context = {
        'car': car,
    }
    return render(request, 'admin_index.html', context)


# order

def reservation_list(request):
    reservation = Reservation.objects.all()

    query = request.GET.get('q')
    if query:
        reservation = reservation.filter(
            Q(pickUpLocation__icontains=query) |
            Q(returnLocation__icontains=query) |
            Q(pickUpDate__icontains=query) |
            Q(returnDate__icontains=query)
        )

    # pagination
    paginator = Paginator(reservation, 4)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        reservation = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        reservation = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        reservation = paginator.page(paginator.num_pages)
    context = {
        'reservation': reservation,
    }
    return render(request, 'reservation_list.html', context)


def reservation_detail(request, id=None):
    detail = get_object_or_404(Reservation, id=id)
    context = {
        "detail": detail,
    }
    return render(request, 'reservation_detail.html', context)


def reservation_created(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "Create Reservation"
    }
    return render(request, 'reservation_create.html', context)


def reservation_update(request, id=None):
    detail = get_object_or_404(Reservation, id=id)
    form = ReservationForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update Reservation"
    }
    return render(request, 'reservation_create.html', context)


def reservation_delete(request, id=None):
    query = get_object_or_404(Reservation, id=id)
    query.delete()
    return HttpResponseRedirect("/listReservation/")

def view_my_reservation(request):
    username = request.user
    user = User.objects.get(username=username)
    car_dealer = CarDealer.objects.get(car_dealer = user)
    reservations = Reservation.objects.filter(car_dealer = car_dealer)
    reservation_list = []
    for r in reservations:
        if r.is_complete == False:
            reservation_list.append(r)
    return render(request,'car_dealer/reservation_list.html', {'reservation_list':reservation_list})



@login_required()
def newCar(request):
    new = Car.objects.order_by('-id')
    # search
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(carName__icontains=query) |
            Q(model__icontains=query) |
            Q(numOfSeats__icontains=query) |
            Q(numOfDoors__icontains=query)|
            Q(transmission=query) |
            Q(airconditioner__icontains=query) |
            Q(price__icontains=query) |
            Q(carStatus__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)


def like_update(request, id=None):
    new = Car.objects.order_by('-id')
    like_count = get_object_or_404(Car, id=id)
    like_count.like += 1
    like_count.save()
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)


def popular_car(request):
    new = Car.objects.order_by('-like')
    # search
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(carName__icontains=query) |
            Q(model__icontains=query) |
            Q(numOfSeats__icontains=query) |
            Q(numOfDoors__icontains=query)|
            Q(transmission=query) |
            Q(airconditioner__icontains=query) |
            Q(price__icontains=query) |
            Q(carStatus__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)


def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/car/newcar/")
    context = {
        "form": form,
        "title": "Contact With Us",
    }
    return render(request, 'contact.html', context)


# -----------------Admin Section-----------------

def admin_car_list(request):
    car = Car.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        car = car.filter(
            Q(carName__icontains=query) |
            Q(model__icontains=query) |
            Q(numOfSeats__icontains=query) |
            Q(numOfDoors__icontains=query)|
            Q(transmission=query) |
            Q(airconditioner__icontains=query) |
            Q(price__icontains=query) |
            Q(carStatus__icontains=query)
        )

    # pagination
    paginator = Paginator(car, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        car = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car = paginator.page(paginator.num_pages)
    context = {
        'car': car,
    }
    return render(request, 'admin_index.html', context)


def admin_msg(request):
    msg = PrivateMsg.objects.order_by('-id')
    context = {
        "car": msg,
    }
    return render(request, 'admin_msg.html', context)


def msg_delete(request, id=None):
    query = get_object_or_404(PrivateMsg, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")


#fonksiyon kontrol demom sonra üzerinde oynayacağım -buse
def dashboard_car_list(request):
    cars = Car.view_car_list()
    car_detail = Car.view_car_detail(3)

    context = {
        "car_details": car_detail,
        "cars": cars
    }

    return render(request, 'car_detail.html', context)

def users(request):
    context = {}
    context["dataset"] =User.objects.all()

    return render(request,'users.html', context)


def profile(request, pk):
    profile = Profile.objects.get(user_id=pk)
    return render(request, 'profile.html', {'profile': profile})
