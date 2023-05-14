from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer_username = models.CharField(max_length=20)
    customer_password = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=50)
    customer_first_name = models.CharField(max_length=40)
    customer_last_name = models.CharField(max_length=40)
    customer_street = models.CharField(max_length=50)
    customer_city = models.CharField(max_length=50)
    customer_zipcode = models.CharField(max_length=50)
    customer_phone_number = models.CharField(max_length=10)
    customer_credit_card_number = models.CharField(max_length=16)
    customer_card_expiry = models.CharField(max_length=6)
    customer_credit_card_cvv = models.IntegerField()

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name} - {self.customer_email}"


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.full_name}, {self.house_no}, {self.street}, {self.landmark}, {self.city}, {self.pincode}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
