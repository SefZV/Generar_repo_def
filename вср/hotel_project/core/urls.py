from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('/stats/', views.ListViewsStats.as_view(), name='stats'), 
    path('/currency/', views.currency_view, name='currency'),
    path('/weather/', views.weather_view, name='weather'),
]