from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("signup",views.sign_user,name="signup"),
    path("login",views.login_user,name="login"),
    path("contact",views.contact,name="contact")
]
