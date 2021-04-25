from django.contrib import admin
from django.urls import path, include
from sedan.views import *


app_name = 'upload'
urlpatterns = [
    path('upload/', DataCreateView.as_view()),
    path('view/', TableView.as_view()),
    path('edit/<int:pk>', Table_View_Editing.as_view()),
    path('store/', TableView.store),
]