from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('car_list/', views.car_list, name='car_list'),

]