from django.shortcuts import render
import pandas as pd

from rest_framework import generics
from sedan.serializers import Data_uploader, Data_view_serializer
from sedan.models import Data_stor, Client
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
class DataCreateView(generics.CreateAPIView):
    serializer_class = Data_uploader
    permission_classes = (IsAuthenticated,)


class TableView(generics.ListAPIView):
    serializer_class = Data_view_serializer
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)

class Table_View_Editing(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Data_uploader
    queryset = Data_stor.objects.all()
    permission_classes = (IsAuthenticated,)


class TableView(generics.CreateAPIView):
    serializer_class = Data_view_serializer
    queryset = Data_stor.objects.all()
    permission_classes = (IsAuthenticated,)

    def store(self):
        data = pd.read_excel(r'E:\SEDAN\eestech-hack-app\data.xlsx',sheet_name=None)
        for c in data.iterrows()[1]:
            c = Client(fio = c[0],sex = c[1],
                        age = c[2],
                        phone =c[3], email= c[4] )
            c.save()
        return c.save()