from rest_framework import serializers

from apps.expense_manager.models import *

class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields = ('id', 'ruc', 'business_name', 'address')
        
    def save(self):
        new_object = Supplier(**self.validated_data)
        return new_object.save()
    
class VoucherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Voucher
        fields = ('id', 'name')
    
class PaymentTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PaymentType
        fields = ('id', 'name')
        

        