from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from sedan.views import *


app_name = 'Client'
urlpatterns = [
    path('Client/create', DataCreateView.as_view()),
    path('accounts/', include('allauth.urls'))
    # path('login/', auth_views.LoginView.as_view()),
    # path('register/', user_views.register, name='register')
    # url(r'^accounts/', include('allauth.urls'))
]

