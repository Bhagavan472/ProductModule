from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
     path("add",views.add),
    path("",views.search),
    path("productid/<int:id>",views.productid),
    path("products",views.products)
]

