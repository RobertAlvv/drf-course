from rest_framework import status
from tests.test_setup import TestSetUp
from apps.expense_manager.test.factories.expense_factory import SupplierFactory


class ExpenseTestCase(TestSetUp):
    
    url = "/expense/expense"
    
    def test_search_supplier(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + "/search_supplier/",
            {
                "ruc_or_business_name": supplier.ruc
            },
            format="json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["RUC"], supplier.ruc)
        
    def test_search_supplier_error(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + "/search_supplier/",
            {
                "ruc_or_business_name": "12312341"                
            },
            format="json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(supplier.ruc, "12312341")
        self.assertEqual(response.data["error"], "No existe el suplidor")