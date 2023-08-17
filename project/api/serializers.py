from rest_framework import serializers
from .models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Shop
        fields = ('name', 'shop_established', 'owner')
    
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'