from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('country-list/', views.country_list, name='countries'),
    path('country/<str:country>', views.country, name='country')
]
