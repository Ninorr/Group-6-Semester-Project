from django.db import models
from .service import Services
from .orders import Order
from django.contrib.auth.models import User
import datetime
import uuid


class Invoice(models.Model):
    order_id = order_id = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    total_price = models.IntegerField()

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_invoice_by_order(order_id):
        return Invoice.objects.filter(order_id=order_id).order_by('-date')

