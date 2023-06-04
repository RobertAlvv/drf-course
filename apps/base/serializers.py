from rest_framework import generics

class BaseGenericAPIView(generics.GenericAPIView):
    serializer_class = None
    
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True)