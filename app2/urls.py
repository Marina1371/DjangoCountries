from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('country-list/', views.country_list, name='countries'),
    path('country/<str:name>', views.country, name='country'),
    path('languages/', views.languages, name='languages'),
    path('language/<str:name>', views.language, name='language'),
    path('countries/<str:letter>', views.countries_letter, name='countries-by-letter')
]
