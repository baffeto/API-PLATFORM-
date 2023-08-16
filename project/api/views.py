from .models import Shop, Product
from .serializers import ShopSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# ModelViewSet - полный функционал GET | POST | PUT | DELETE
# ReadOnlyModelViewSet - только чтение GET

class ShopViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ProductViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer