from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('api/books/', views.books, name='book-list'),
    path('api/customers/', views.customers, name='customer-list')
]


