from django.contrib import admin
from django.urls import path, include
from sedan.views import *


app_name = 'Client'
urlpatterns = [
    path('Client/create', DataCreateView.as_view())
]