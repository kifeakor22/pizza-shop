from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     path('add/<int:product_id>/', views.add_cart, name='add_cart'),
     path('',views.cart_detail, name='cart_detail'),
]
