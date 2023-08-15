from .models import Shop, Product
from .serializers import ShopSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ShopAPIView(APIView):
    def get(self, request):
        list_shops = Shop.objects.all()
        
        return Response({
            'shops': ShopSerializer(list_shops, many=True).data
        })
        
    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'shop': serializer.data
        })

    def put(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({
                'error': 'Method put not allowed!'
            })
        
        try:
            instance = Shop.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Object does not exists!'
            })
            
        serializer = ShopSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'shop': serializer.data
        })
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({
                'error':
                    'Method delete not allowed!'
                })
            
        shop = Shop.objects.get(pk=pk)
        shop.delete()
            
        return Response({
            'shop': 'delete shop ' + str(pk)
        })
    
    
class ProductAPIView(APIView):
    def get(self, request):
        list_products = Product.objects.all()
        
        return Response({
            'product': ProductSerializer(list_products, many=True).data
        })
        
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'product': serializer.data
        })

    def put(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({
                'error': 'Method put not allowed!'
            })
        
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Object does not exists!'
            })
            
        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'product': serializer.data
        })
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({
                'error':
                    'Method delete not allowed!'
                })
            
        product = Product.objects.get(pk=pk)
        product.delete()
            
        return Response({
            'product': 'delete product ' + str(pk)
        })
    
    