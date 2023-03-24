from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/services', views.services, name='services'),
    path('aboutus/contactus',views.contactus, name='contactus'),
    path('aboutus/whoweare',views.whoweare, name='whoweare'),
]
