from .models import Shop, Product
from .serializers import ShopSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

# Get и Post запросы
class ShopAPIList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Get (определенный) / PUT / DELETE (работаем с определенным объектом)    
class ShopAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer 

class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 