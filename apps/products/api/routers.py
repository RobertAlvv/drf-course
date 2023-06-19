from rest_framework.routers import DefaultRouter
from .views.product_viewsets import ProductViewSet
from .views.general_view import *

routers = DefaultRouter()
routers.register('products', ProductViewSet, basename= 'products')
routers.register('measure-unit', MeasureUnitViewset, basename= 'measure')
routers.register('indicators', IndicatorListViewset, basename= 'indicators')
routers.register('category-products', CategoryProductViewset, basename= 'category')

urlpatterns = routers.urls

