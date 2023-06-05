from apps.base.views import BaseGenericListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer

class MeasureUnitListAPIView(BaseGenericListAPIView):
    serializer_class = MeasureUnitSerializer
    
class CategoryProductListAPIView(BaseGenericListAPIView):
    serializer_class = CategoryProductSerializer
    
class IndicatorListAPIView(BaseGenericListAPIView):
    serializer_class = IndicatorSerializer