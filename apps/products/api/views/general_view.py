from apps.base.serializers import BaseGenericAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
from apps.products.models import MeasureUnit, CategoryProduct, Indicator

class MeasureUnitListAPIView(BaseGenericAPIView):
    serializer_class = MeasureUnitSerializer
    
class CategoryProductListAPIView(BaseGenericAPIView):
    serializer_class = CategoryProductSerializer
    
class IndicatorListAPIView(BaseGenericAPIView):
    serializer_class = IndicatorSerializer