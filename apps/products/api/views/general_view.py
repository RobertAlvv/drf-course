from rest_framework import viewsets
from rest_framework.response import Response

from apps.products.models import MeasureUnit
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer

class MeasureUnitViewset(viewsets.GenericViewSet):
    serializer_class = MeasureUnitSerializer
    model = MeasureUnit
    
    def get_queryset(self):
        return super().get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
    
    
class CategoryProductViewset(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer
    
class IndicatorListViewset(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer