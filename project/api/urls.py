from .views import ShopAPIList, ShopAPIDetailView, ProductAPIList, ProductAPIDetailView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('list/shops/', ShopAPIList.as_view()),
    path('list/products/', ProductAPIList.as_view()),
    path('shop/<int:pk>/', ShopAPIDetailView.as_view()),
    path('product/<int:pk>/', ProductAPIDetailView.as_view()),
]