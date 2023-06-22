from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
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
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs["pk"] ,state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Categoria registrada correctamente!"}, status = status.HTTP_200_OK)
        return Response({"message": "", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_object.exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Categoria actualizada correctamente"}, status=status.http_200)
        return Response({"message": "","error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().state = True
            return Response({"message": "Categoria eliminada correctamente"}, status=status.HTTP_200_OK)
        return Response({"message": "", "error":"Categoria no encontrada"}, status=status.HTTP_400_BAD_REQUEST)    
               
        
class IndicatorListViewset(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer