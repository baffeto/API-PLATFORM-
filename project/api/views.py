from .models import Shop, Product
from .serializers import ShopSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
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
    
    # queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        
        if not pk:
            return Shop.objects.all()[:6]
        
        return Shop.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=True)
    def product(self, request, pk=None):
        # http://127.0.0.1:8000/api/v1/shop/4/product/
        product = Product.objects.get(pk=pk)
        return Response({
            'product': product.name
        })

class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer