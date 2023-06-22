from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.views.static import serve

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import Login, Logout

schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion de API",
        default_version="v0.1",
        description="Documentacion publica de API de Ecommerce",
        terms_of_service="",
        contact=openapi.Contact(email="alvarezrobert150@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('users/', include('apps.users.api.routers')),
    path('products/', include('apps.products.api.routers')),
    path('expenses/', include('apps.expense_manager.api.routers')),
]


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    }),
]