from django.db import models
from .service import Services
from django.contrib.auth.models import User
import datetime
import uuid


class Order(models.Model):
    service = models.ForeignKey(Services,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_id = models.CharField(max_length=100, default='', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    @staticmethod
    def get_orders_by_orderid(orderid):
        return Order.objects.filter(order_id=orderid).order_by('-date')

