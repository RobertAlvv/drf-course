from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    measure_unit = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        exclude = ('state','created_date', 'modified_date', 'deleted_date',)
        
    def to_representation(self, instance): 
        return {
            'id': instance.id,
            'description': '' if not instance.description else instance.description,
            'image': '' if not instance.image.url else instance.image,
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description,
        }