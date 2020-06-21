from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.index, name='client'),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('add_policy',views.addpolicy,name='add_policy'),
    path('',views.image,name='image'),
]
