from background_task.models import Task
from django.urls import path
from . import views
from .views import clean_completed_reservations

urlpatterns = [
    path('', views.home, name='home'),
    path('car/list/', views.car_list, name='car_list'),
    path('cars/available', views.available_cars, name='available_cars'),
    path('users/', views.users, name='users'),
    path('profile/<int:pk>', views.view_profile, name='profile'),
    path('profile/edit/<int:pk>', views.edit_profile, name='edit_profile'),
    path('reservations/list', views.reservation_list, name='reservation_list'),
    path('reservations/<int:car_id>/<str:pickUpLocation>/<str:returnLocation>/<str:pickUpDate>/<str:returnDate>',
         views.create_reservation, name='reservation_create'),
    path('reservation/approve', views.complete_reservation, name='reservation_approve'),
    path('contact/', views.contact, name='contact'),
    path('reservations/cardealer', views.view_my_reservation_cardealer, name='cardealer_reservations'),
    path('reservations/customer', views.view_my_reservation_customer, name='customer_reservations'),
    path('car/create/', views.create_car, name='create_car'),
    path('car/delete/<int:pk>', views.car_delete, name='car_delete'),
    path('car/update/<int:pk>', views.car_update, name='car_update'),
    path('reservations/delete/customer/<int:pk>', views.reservation_delete, name='reservation_delete'),
    path('admin/dashboard', views.total_car_list, name='total_car_list'),
    path('reservations/admin', views.reservation_list, name='reservation_list'),
    path('admin/user/approve/<int:pk>', views.car_dealer_approve, name='reservation_list'),
    path('branch/add', views.add_branch, name='add_branch'),
    path('branch/list', views.branch_list, name='branch_list'),
    path('branch/delete/<int:pk>', views.branch_delete, name='branch_delete'),
    path('branch/update/<int:pk>', views.branch_update, name='branch_update'),
    path('branch/branch_car_list/<int:pk>', views.branch_car_list, name='branch_car_list'),
    path('admin/cardealerdelete/<int:pk>', views.CarDealer_delete, name='CarDealer_delete'),
    path('admin/user/delete/<int:pk>', views.car_dealer_reject, name='car_dealer_reject'),
    path('delete/notification/<int:pk>', views.delete_notification, name='delete_notification'),
    path('reservations/customer/history', views.view_my_reservation_customer_history, name='my_reservation_customer_history'),
    path('reservations/cardealer/history', views.view_my_reservation_cardealer_history, name='my_reservation_cardealer_history'),
    path('reservations/admin/history', views.view_my_reservation_admin_history, name='my_reservation_admin_history'),



]

clean_completed_reservations(repeat=10)