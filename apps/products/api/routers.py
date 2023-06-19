from rest_framework.routers import DefaultRouter
from .views.product_viewsets import ProductViewSet

routers = DefaultRouter()
routers.register('products', ProductViewSet, basename= 'products')

urlpatterns = routers.urls

