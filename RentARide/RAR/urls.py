
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='redirect'),
    path('home/', views.home, name='home'),
    path('car_list/', views.car_list, name='car_list'),
    path('demo/', views.dashboard_car_list, name='demo'),
    path('users/', views.users, name='users'),
    path('profile/<slug:pk>', views.profile, name='profile'),
]