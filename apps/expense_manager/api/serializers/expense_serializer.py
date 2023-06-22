from rest_framework import serializers
from apps.expense_manager.models import Expense, Supplier


class SupplierRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        exclude = ('state', 'created_at', 'modified_date', 'deleted_date')

class ExpenseSerializer(serializers.Serializer):
    
    class Meta:
        model = Expense
        exclude = ('state', 'created_at', 'modified_date', 'deleted_date')
        




        