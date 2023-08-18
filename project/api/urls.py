from .views import ShopAPIDestroy, ShopAPIList, ShopAPIUpdate, ProductAPIList, ProductAPIUpdate, ProductAPIDestroy
from django.urls import path


app_name = 'api'

urlpatterns = [
    path('shop/', ShopAPIList.as_view()),
    path('shop/<int:pk>/', ShopAPIUpdate.as_view()),
    path('shop/delete/<int:pk>/', ShopAPIDestroy.as_view()),
    path('product/', ProductAPIList.as_view()),
    path('product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('product/delete/<int:pk>/', ProductAPIDestroy.as_view()),
]