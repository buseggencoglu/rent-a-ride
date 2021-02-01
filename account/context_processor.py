from django.contrib.auth.models import AnonymousUser

from RAR.models import Customer, CarDealer, Notifications


def user_type(request):
    user = request.user
    if not user.is_anonymous:
        customers = Customer.objects.filter(user=user)
        car_dealers = CarDealer.objects.filter(user=user)
        notifications = Notifications.objects.filter(user=user)
        user_type = 'admin'
        if len(customers) > 0:
            user_type = 'customer'
        elif len(car_dealers) > 0:
            user_type= 'car_dealer'
        return {
            'user': user,
            'user_type': user_type,
            'notifications': notifications
        }
    return {}
