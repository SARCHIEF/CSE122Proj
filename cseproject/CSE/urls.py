from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= 'index'),
    path("learn", views.learn, name= "learn"),
    path("develope", views.develope, name="develope"),
    path("sell", views.sell, name="sell"),
    path("contacts", views.contacts, name="contacts"),

]
