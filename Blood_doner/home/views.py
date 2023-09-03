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
            dnr = Doner(user_name=name,contact_no=phone,blood_group=blood,state=state,city=city,slug=name)
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
            user_log = authenticate(username=f_name,password=password)
            login(request, user_log)
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
            return redirect("/login")
            messages.error(request,"Please enter correct information")
    return render(request,'login.html')

def search(request):
    blood = request.GET['blood_group']
    state = request.GET['state']
    cty = request.GET['cty']
    alldonerbloodgroup = Doner.objects.filter(blood_group__exact=blood)
    alldonerstate = Doner.objects.filter(state__exact=state)
    alldonercity = Doner.objects.filter(city__exact=cty)
    total = alldonercity.union(alldonerbloodgroup,alldonerstate)
    params = {'total':total}
    return render(request,'search.html',params)

def delete_post(request,slug):
    doner = Doner.objects.get(slug=slug)
    doner.delete()
    return redirect("/")