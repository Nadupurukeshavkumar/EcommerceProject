from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('api-data/', views.api_data, name='api_data'),
]
