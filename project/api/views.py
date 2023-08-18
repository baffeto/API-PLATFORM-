from .models import Shop, Product
from .serializers import ShopSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
    
    
class ShopAPIList(generics.ListCreateAPIView):
    queryset =  Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
class ShopAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset =  Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    
class ShopAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset =  Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAdminOrReadOnly, )
    
class ProductAPIList(generics.ListCreateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    
class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )