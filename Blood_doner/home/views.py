from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from home.models import Doner
import math


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        blood = request.POST.get('blood')
        state = request.POST.get('state')
        city = request.POST.get('city')
        if(phone is str):
            messages.error(request,"please enter a valid number")
        else:
            dnr = Doner(user_name=name,contact_no=phone,blood_group=blood,state=state,city=city)
            messages.success(request,"Thanks for being a doner")
            dnr.save()
    all_doners = Doner.objects.all()
    context = {'doners':all_doners}
    return render(request,'index.html',context)

def sign_user(request):
    if request.method == "POST":
        f_name = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_con = request.POST.get('password_con')
        if password != password_con:
            messages.error(request,"passwords do not match")
        else:
            user = User.objects.create_user(username=f_name,email=email,password=password)
            messages.success(request,"signed up successfully")
            user.save()
            return redirect("/")
    return render(request,'signup.html')

def contact(request):
    return render(request,'contact.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"you are logged in successfully")
            return redirect("/")
        elif user is None:
            messages.error(request,"Please enter correct information")
            return redirect("/")
    return render(request,'login.html')