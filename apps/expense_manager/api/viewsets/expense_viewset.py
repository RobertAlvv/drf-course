from django.db.models import Q

from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.products.models import Product
from apps.expense_manager.models import *
from apps.base.utils.format_date import format_date
from apps.expense_manager.api.serializers.expense_serializer import *
from apps.expense_manager.api.serializers.general_serializer import *


class ExpenseViewset(GenericViewSet):
    serializer_class = ExpenseSerializer
    
    @action(methods=["get"], detail=False)
    def search_supplier(self, request):
        ruc_or_business_name = request.query_params.get('ruc_or_business_name', '')
        supplier = Supplier.objects.filter(
            Q(ruc__iexact=ruc_or_business_name) | 
            Q(business_name__iexact=ruc_or_business_name)
        ).first()
        
        if supplier:
            supplier_serializer = SupplierSerializer(supplier)
            return Response(supplier_serializer.data, status = status.HTTP_200_OK)
        
        return Response({"error":"No existe el suplidor"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['post'], detail=False)
    def new_suplier(self, request):
        supplier_serializer = SupplierRegisterSerializer(data = request.data)
        if supplier_serializer.is_valid():
            supplier_serializer.save()
            Response(supplier_serializer.data, status=status.HTTP_200_OK)
        Response(supplier_serializer.error_messages, status=status.HTTP_400_BAD_REQUEST )
    
    
    @action(methods=["get"], detail=False)
    def get_vouchers(self, request):
        data = Voucher.objects.filter(state=True).order_by("id")
        data = VoucherSerializer(data=data, many=True).data
        return Response(data)

    @action(methods=["get"], detail=False)
    def get_payment_type(self, request):
        data = PaymentType.objects.filter(state=True).order_by("id")
        data = PaymentTypeSerializer(data=data, many=True).data
        return Response(data)
    
    @action(methods=["get"], detail=False)
    def get_product(self, request):
        data = Product.objects.filter(state=True).order_by("id")
        data = ProductSerializer(data=data, many=True).data
        return Response(data)
    
    def format_data(self, data):
        JWT_authentication = JWTAuthentication()
        user, _ = JWT_authentication.authentication(self.request)
        data["user"] = user.id
        data["date"] = format_date(data["date"])
        return data
    
    def create(self, request):
        data = request.data
        data = self.format_data(request.data)
        expense_serializer = self.serializer_class(data=data)
        if expense_serializer.is_valid():
            expense_serializer.save()
            return Response({"message": "Factura registrada correctamente"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"message": "Han ocurridos errores en la creacion", "errors": expense_serializer.errors},status=status.HTTP_400_BAD_REQUEST)