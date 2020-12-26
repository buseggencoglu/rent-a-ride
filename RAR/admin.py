from django.contrib import admin
from .models import Car, Reservation, PrivateMsg, Admin, Branch,CarDealer, Customer


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("carName", "model")


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("car", "pickUpDate", "returnDate", "carDealer")


class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")


admin.site.register(Car, CarAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)
#admin.site.register(CustomUser)
#admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Branch)
admin.site.register(CarDealer)
admin.site.register(Customer)
#admin.site.register(CarDealerCustomerSystem)
#admin.site.register(Profile)