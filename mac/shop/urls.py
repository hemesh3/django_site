from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name='shop_index'),
    path("about", views.about,name='shop_about'),
    path("cart", views.cart,name='shop_cart'),
]
