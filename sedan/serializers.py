from rest_framework import serializers
from sedan.models import  Data_stor

class Data_uploader(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #Скрываем поле юзер, автоматически вставляет из реквеста
    class Meta:
        model = Data_stor
        fields = '__all__'

class Data_view_serializer(serializers.ModelSerializer):
    class Meta:
        model = Data_stor
        fields = '__all__'