from django.contrib import admin
from .models import Car, Reservation, PrivateMsg, User, Admin, Branch,CarDealer


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("carName", "model")


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("carID", "pickUpDate", "returnDate", "carDealerID")


class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")


admin.site.register(Car, CarAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Branch)
admin.site.register(CarDealer)