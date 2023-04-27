from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.views import View
from store.models.service import Services
from store.models.orders import Order


class OrderView(View):


    def get(self , request ):
        customer = request.user
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
