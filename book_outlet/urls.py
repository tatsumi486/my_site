from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="books_home"),
    path("<slug:slug>", views.book_deets, name="book_details")
]
