from django.contrib import admin
from django.urls import path, include
from .views.home import Index, store
from django.conf import settings
from django.conf.urls.static import static
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.invoices import InvoiceView
from .views.invoiceList import InvoiceListView
from .views.invoiceDetails import InvoiceDetailsView


urlpatterns = [
    path('services', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    path('invoices', InvoiceView.as_view(), name='invoices'),
    path('invoiceDetails/<str:order_id>', InvoiceDetailsView.as_view(), name='InvoiceDetails'),
    path('invoiceList', InvoiceListView.as_view(), name='invoiceList'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
