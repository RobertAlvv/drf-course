from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.base.views import BaseGenericListAPIView

class ProductListAPIView(BaseGenericListAPIView):
    serializer_class = ProductSerializer