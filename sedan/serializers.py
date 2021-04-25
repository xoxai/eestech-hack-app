from rest_framework import serializers
from sedan.models import  Data_stor, Client

class Data_uploader(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #Скрываем поле юзер, автоматически вставляет из реквеста
    class Meta:
        model = Data_stor, Client
        fields = '__all__'

class Data_view_serializer(serializers.ModelSerializer):
    class Meta:
        model = Data_stor
        fields = '__all__'