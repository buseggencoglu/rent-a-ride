
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('car_list/', views.car_list, name='car_list'),
    path('demo/', views.dashboard_car_list, name='demo'),
    path('users/', views.users, name='users'),
    path('profile/<slug:pk>', views.profile, name='profile'),
    path('reservation_list/', views.reservation_list, name='reservation_list'),
    path('contact/', views.contact, name='contact'),
    path('my_reservations/', views.view_my_reservation_cardealer, name='my_reservations'),
    path('my_reservations/', views.view_my_reservation_customer, name='my_reservations'),
    path('index/', views.index, name='index'),
    path('search_results/', views.search_results, name='search_results'),
    path('search/', views.search, name='search'),

]