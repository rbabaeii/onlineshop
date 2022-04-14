
from rest_framework import serializers
from . import models


class FoodsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Food
        fields = ['id', 'name', 'price', 'description', 'image']
class New_orderserializer(serializers.ModelSerializer):
    class Meta :
        model = models.New_order
        fields = "__all__"