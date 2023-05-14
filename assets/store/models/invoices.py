from django.db import models
from .service import Services
from .orders import Order
from django.contrib.auth.models import User
from .orders import Order
import datetime
import uuid


class Invoice(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    #order_id = order_id = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_invoice_by_order(order_id):
        return Invoice.objects.filter(order_id=order_id).order_by('-date')

    @staticmethod
    def get_invoice_by_order_ids(order_ids):
        invoices = []
        for order_id in order_ids:
            invoice_obj = Invoice.objects.filter(order_id=order_id)
            invoices.append(invoice_obj[0])
        return invoices

