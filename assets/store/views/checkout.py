from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.views import View

from store.models.service import Services
from store.models.orders import Order
from store.models.invoices import Invoice
import uuid
from store.templatetags import cart


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        ##customer = request.session.get('customer')
        user_name = request.user.get_username()
        session_cart = request.session.get('cart')
        services = Services.get_service_by_id(list(session_cart.keys()))
        print(address, phone, user_name, session_cart, services)
        orderid = str(uuid.uuid4())
        request.session['orderid'] = orderid
        for service in services:
            print(session_cart.get(str(service.id)))
            print(request.user.username )
            order = Order(customer=User(id=request.user.id),
                          service=service,
                          order_id=orderid,
                          price=service.price,
                          address=address,
                          phone=phone,
                          quantity=session_cart.get(str(service.id)))
            order.save()
        total = cart.total_cart_price(services, session_cart)
        invoice = Invoice(order_id=orderid,
                      total_price=total,
                      )
        invoice.save()
        request.session['cart'] = {}

        #return redirect('cart')
        return render(request, 'check_out.html')
