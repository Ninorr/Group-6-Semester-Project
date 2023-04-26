from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddressForm
from .models import Address


def index(request):
    return render(request, 'index.html', )


def services(request):
    return render(request, 'services.html', )


def contactus(request):
    return render(request, 'contact.html', )


def whoweare(request):
    return render(request, 'whoweare.html', )


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['uemail']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        password = request.POST['passkey']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "Your account has been created successfully!")

        return render(request, 'registration/login.html')

    return render(request, 'registration/signup.html')


def home(request):
    return render(request, 'registration/home.html')


@login_required()
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'address_list.html', {'addresses': addresses})


@login_required()
def address_create(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        address = form.save(commit=False)  # create an unsaved Address object from the form data
        address.user = request.user  # set the user_id field to the current user
        address.save()  # save the Address object to the database
        return redirect('address_list')
    return render(request, 'address_form.html', {'form': form})


def address_update(request, pk):
    address = get_object_or_404(Address, pk=pk)
    form = AddressForm(request.POST or None, instance=address)
    if form.is_valid():
        form.save()
        return redirect('address_list')
    return render(request, 'address_form.html', {'form': form})


def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('address_list')
    return render(request, 'address_confirm_delete.html', {'address': address})


@login_required
def change_name(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.username = request.POST.get('username', '')
        user.save()
        return redirect('change_name')

    return render(request, 'myaccount.html')


def myaccount(request):
    return render(request, 'myaccount.html')


def terms(request):
    return render(request, 'terms.html', )


@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        messages.success(request, 'Your account has been deleted.')
        return redirect('signup')
    return render(request, 'delete_account.html')
