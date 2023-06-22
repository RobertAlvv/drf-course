from rest_framework.routers import DefaultRouter

from apps.expense_manager.api.viewsets.expense_viewset import ExpenseViewset

router = DefaultRouter()

router.register("expense",ExpenseViewset, basename="expense")

urlpatterns = router.urls