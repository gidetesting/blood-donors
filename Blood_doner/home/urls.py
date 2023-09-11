from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("signup",views.sign_user,name="signup"),
    path("login",views.login_user,name="login"),
    path("search",views.search,name="search"),
    path("contact",views.contact,name="contact"),
    path('delete/<str:slug>',views.delete_post,name='delpost'),
    path('del_conf',views.del_conf,name="conformation"),
    path('donor_posted/<str:username>/', views.donor_posted, name='donor_has_posted'),
]
