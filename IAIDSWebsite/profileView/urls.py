from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.profileView, name='profileView'),
]