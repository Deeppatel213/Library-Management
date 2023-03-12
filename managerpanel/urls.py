from django.contrib import admin
from django.urls import path
from managerpanel import views

urlpatterns = [
    path('', views.adminpanel),
]