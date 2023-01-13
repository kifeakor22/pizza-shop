from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path('signup_view', views.signup_view, name="signup"),
    path("home", views.home, name="home"),
    path("logout_view", views.logout_view, name="logout"),
    path("order", views.order, name="order")
]
