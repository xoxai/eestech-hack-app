from django.shortcuts import render
from rest_framework import generics
from sedan.serializers import Data_uploader, Data_view_serializer
from sedan.models import Data_stor
from rest_framework.permissions import IsAuthenticated,
# Create your views here.
class DataCreateView(generics.CreateAPIView):
    serializer_class = Data_uploader
    permission_classes = (IsAuthenticated,)

class TableView(generics.ListAPIView):
    serializer_class = Data_view_serializer
    queryset = Data_stor.objects.all()
    permission_classes = (IsAuthenticated,)

class Table_View_Editing(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Data_uploader
    queryset = Data_stor.objects.all()
    permission_classes = (IsAuthenticated,)
