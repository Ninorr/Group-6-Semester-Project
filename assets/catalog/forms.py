from django import forms
from .models import Address
from .models import Review


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'mobile', 'pincode', 'house_no', 'street', 'landmark', 'city']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
