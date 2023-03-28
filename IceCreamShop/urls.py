from django.contrib import admin
from django.urls import path
from IceCreamShop import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("contact/", views.contact_page, name="contact")
]
