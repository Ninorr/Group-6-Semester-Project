from django.contrib import admin
from django.urls import path, include
from .views.home import Index, store
from django.conf import settings
from django.conf.urls.static import static
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView


urlpatterns = [
    path('services', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
