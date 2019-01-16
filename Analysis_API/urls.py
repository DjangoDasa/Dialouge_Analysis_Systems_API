from django.contrib import admin
from django.urls import path
from .views import home_view, index

urlpatterns = [
    path('', home_view, name='home'),
    path()
]


