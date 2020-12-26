
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('users/', views.users, name='users'),
    path('profile/<slug:pk>', views.profile, name='profile'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('contact/', views.contact, name='contact'),
    path('cardealer/reservations/', views.view_my_reservation_cardealer, name='cardealer_reservations'),
    path('customer/reservations/', views.view_my_reservation_customer, name='customer_reservations'),
    path('car/create/', views.create_car, name='create_car'),
    path('car/delete/<int:pk>', views.car_delete, name='car_delete'),
    path('car/update/<int:pk>', views.car_update, name='car_update'),
]
