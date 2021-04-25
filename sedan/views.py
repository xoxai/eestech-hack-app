from django.shortcuts import render
from rest_framework import generics
from sedan.serializers import Data_uploader
# Create your views here.
class DataCreateView(generics.CreateAPIView):
    serializer_class = Data_uploader

