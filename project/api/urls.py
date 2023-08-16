from .views import ShopViewSet, ProductViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'shop', ShopViewSet)
router.register(r'product', ProductViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)), # api/v1/shop | api/v1/product
]