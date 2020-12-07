from django.contrib import admin
from .models import Car, Reservation, PrivateMsg

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("carName", "image", "userID")


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("carID", "pickUpDate", "returnDate", "carDealerID")


class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")


admin.site.register(Car, CarAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)