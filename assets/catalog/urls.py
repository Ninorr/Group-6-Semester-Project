from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.index, name='index'),
    path('aboutus/services', views.services, name='services'),
    path('aboutus/contactus',views.contactus, name='contactus'),
    path('aboutus/whoweare',views.whoweare, name='whoweare'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name="signup"),
    path('home', views.home, name="home"),
]
