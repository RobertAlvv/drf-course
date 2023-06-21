from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.users.authentication_mixins import Authentication
from apps.products.api.serializers.product_serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def update(self, request, pk = None):
       product = self.get_queryset(pk)
       if product:
           product_serializer = self.serializer_class(product, data = request.data)
           if product_serializer.is_valid():
               product_serializer.save()
               return Response(product_serializer.data, status= status.HTTP_200_OK)
           return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
       return Response({'error': 'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST) 
   
    def create(self, request):
        serializer = self.get_serializer()
        serializer = serializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente'}, status= status.HTTP_204_NO_CONTENT)
        return Response({'error': 'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)  
        
         
        
