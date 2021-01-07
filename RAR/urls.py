
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('car/list', views.car_list, name='car_list'),
    path('cars/available', views.available_cars, name='available_cars'),
    path('users/', views.users, name='users'),
    # path('profile/', views.profile, name='profile'),
    path('reservations/list', views.reservation_list, name='reservation_list'),
    path('reservations/<int:car_id>/<str:pickUpLocation>/<str:returnLocation>/<str:pickUpDate>/<str:returnDate>',
         views.create_reservation, name='reservation_create'),
    path('reservation/customer/approve', views.complete_reservation_customer, name='reservation_customer_approve'),
    path('reservation/admin/approve', views.complete_reservation_admin, name='reservation_admin_approve'),
    path('contact/', views.contact, name='contact'),
    path('reservations/cardealer', views.view_my_reservation_cardealer, name='cardealer_reservations'),
    path('reservations/customer', views.view_my_reservation_customer, name='customer_reservations'),
    path('reservations/admin', views.view_my_reservation_admin, name='admin_reservations'),
    path('car/create/', views.create_car, name='create_car'),
    path('car/delete/<int:pk>', views.car_delete, name='car_delete'),
    path('car/update/<int:pk>', views.car_update, name='car_update'),
    path('reservation/update/customer/<int:pk>', views.update_reservation_customer, name='update_reservation_customer'),
    path('reservations/delete/customer/<int:pk>', views.reservation_delete, name='reservation_delete')
]
