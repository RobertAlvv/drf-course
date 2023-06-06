from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.base.views import BaseGenericListAPIView

class ProductListAPIView(BaseGenericListAPIView):
    serializer_class = ProductSerializer
    
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    
    
    def post(self, request):
        serializer = self.get_serializer()
        serializer = serializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)