from rest_framework import serializers
from sedan.models import  Data_stor

class Data_uploader(serializers.ModelSerializer):
    class Meta:
        model = Data_stor
        fields = '__all__'