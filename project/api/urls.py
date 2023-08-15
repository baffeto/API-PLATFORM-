from .views import ShopAPIView, ProductAPIView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('v1/shop/list', ShopAPIView.as_view()),
    path('v1/product/list', ProductAPIView.as_view())
]