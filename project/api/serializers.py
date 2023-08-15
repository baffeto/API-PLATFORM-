from rest_framework import serializers
from .models import Shop, Product


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    shop_established = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Shop.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shop_established = validated_data.get('shop_established', instance.shop_established)
        instance.save()
        return instance
        
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    shop_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.time_create = validated_data.get('time_create', instance.time_create) 
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.save()
        return instance