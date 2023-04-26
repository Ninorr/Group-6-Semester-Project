from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'mobile', 'pincode', 'house_no', 'street', 'landmark', 'city']
