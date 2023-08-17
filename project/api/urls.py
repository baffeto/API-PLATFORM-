from .views import ProductViewSet, ShopAPIDestroy, ShopAPIList, ShopAPIUpdate
from django.urls import path, include
from rest_framework import routers

# SimpleRouter - нет представления всех маршрутов /api/v1/
# DefaultRouter - имеет представление всех маршрутов /api/v1/shop | /api/v1/product

# class MyCustomRouter(routers.DefaultRouter):
#     routes = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]

# router = MyCustomRouter()
router = routers.DefaultRouter()
# router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'product', ProductViewSet)

print(router.urls)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)), # api/v1/shop | api/v1/product
    path('shop/', ShopAPIList.as_view()),
    path('shop/<int:pk>/', ShopAPIUpdate.as_view()),
    path('shop/delete/<int:pk>/', ShopAPIDestroy.as_view())
]