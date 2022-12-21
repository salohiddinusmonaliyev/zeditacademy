from rest_framework.serializers import ModelSerializer

from .models import *

class SuvSerializer(ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id','ism', 'yosh', 'ish_vaqti']

class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

class HaydovchiSerializer(ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'

class BuyurtmaSerializer(ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'