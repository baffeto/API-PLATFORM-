from .views import ShopAPIView, ProductAPIView, ShopAPIList
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('v1/shop/list', ShopAPIList.as_view()),
    path('v1/product/list', ProductAPIView.as_view()),
    path('v1/shop/list/<int:pk>/', ShopAPIList.as_view()),
    path('v1/product/list/<int:pk>/', ProductAPIView.as_view())
]