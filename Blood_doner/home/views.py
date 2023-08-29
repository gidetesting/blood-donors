from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')

def sign_user(request):
    if request.method == "POST":
        f_name = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_con = request.POST.get('password_con')
        user = User.objects.create_user(username=f_name,email=email,password=password)
        if User.objects.filter(username=f_name).exists():
            return redirect("/signup")
            messages.error(request,"this username already exists!")
        elif password != password_con:
            messages.error(request,"Password does not match with each other")
        else:
            messages.success(request,"signed up successfully")
            user.save()
            return redirect("/")
    return render(request,'signup.html')