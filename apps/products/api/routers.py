from rest_framework.routers import DefaultRouter
from .viewsets.product_viewsets import ProductViewSet
from .viewsets.general_view import *

routers = DefaultRouter()
routers.register('products', ProductViewSet, basename= 'products')
routers.register('measure-unit', MeasureUnitViewset, basename= 'measure')
routers.register('indicators', IndicatorListViewset, basename= 'indicators')
routers.register('category-products', CategoryProductViewset, basename= 'category')

urlpatterns = routers.urls

