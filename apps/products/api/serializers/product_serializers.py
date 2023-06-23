from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    measure_unit = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        exclude = ('state','created_date', 'modified_date', 'deleted_date',)
        
        
    def validate_measure_unit(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una unidad de medida")
        return value
        
    def validate_category_product(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe de ingresar una categoria de producto")
        return value
    
    
    def validate(self, data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({"measure_unit": "Debe de ingresar una unidad de medida"})
    
        if 'category_product' not in data.keys():
            raise serializers.ValidationError({"category_product": "Debe de ingresar una categoria de productos"})
        
    def to_representation(self, instance): 
        return {
            'id': instance.id,
            'description': '' if not instance.description else instance.description,
            'image': '' if not instance.image.url else instance.image,
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description,
        }

class ProductRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state','created_date', 'modified_date', 'deleted_date',)
        

