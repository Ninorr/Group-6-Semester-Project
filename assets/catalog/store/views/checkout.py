from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.views import View

from store.models.service import Services
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        ##customer = request.session.get('customer')
        user_name = request.user.get_username()
        cart = request.session.get('cart')
        services = Services.get_service_by_id(list(cart.keys()))
        print(address, phone, user_name, cart, services)

        for service in services:
            print(cart.get(str(service.id)))
            print(request.user.username )
            order = Order(customer=User(id=request.user.id),
                          service=service,
                          price=service.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(service.id)))
            order.save()
        request.session['cart'] = {}

        #return redirect('cart')
        return render(request, 'check_out.html')
