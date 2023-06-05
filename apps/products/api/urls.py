from django.urls import path
# from apps.users.api.view import UserAPIView
from apps.products.api.views.general_view import (MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView)
from apps.products.api.views.product_view import ProductListAPIView
 
urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'), 
    path('category_product/', CategoryProductListAPIView.as_view(), name = 'category_product'), 
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'), 
    path('product/', ProductListAPIView.as_view(), name = 'product'), 
]