from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin



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

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request, "Your account has been created successfully!")

        return render(request,'registration/login.html')

    return render(request,'registration/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user = authenticate(request,username=username,email=email)

        if user is not None:
            auth_login(request, user)
            usern = user.username
            messages.success(request,"Successfully logged in.")
            return redirect("base.html")
        else:
            messages.error(request,"Unable to login")
            return redirect('/login')

    return render(request,'registration/login.html')