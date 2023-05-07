from django.contrib import admin
from .models import Services
from .models import Order
from store.models.invoices import Invoice
# Register your models here.
admin.site.register(Services)
admin.site.register(Order)
admin.site.register(Invoice)
