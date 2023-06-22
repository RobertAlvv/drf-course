from rest_framework.routers import DefaultRouter
from apps.users.api.view import UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")

urlpatterns = router.urls