from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.service import Services


class Cart(View):
    def get(self , request):
        cartobject = request.session.get('cart')
        services = {}
        if cartobject:
            ids = list(request.session.get('cart').keys())
            services = Services.get_service_by_id(ids)
            print(f"Cart_view: {services}")
        return render(request, 'cart.html', {'services': services})

