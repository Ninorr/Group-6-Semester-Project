from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.views import View
from store.models.service import Services
from store.models.orders import Order
from store.models.invoices import Invoice


class InvoiceView(View):


    def get(self , request ):
        orderid = request.session.get('orderid')
        invoice = Invoice.get_invoice_by_order(orderid)
        print(f"invoice: {invoice[0]}")
        orders = Order.get_orders_by_orderid(orderid)
        print(f"orders from invoice view: {orders}")
        return render(request, 'invoice.html', {'orders': orders, 'invoice': invoice[0]})
