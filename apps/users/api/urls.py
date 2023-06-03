from django.urls import path
# from apps.users.api.view import UserAPIView
from apps.users.api.view import user_api_view, user_detail_view

urlpatterns = [
    path('usuarios/', user_api_view, name= 'usuario_api'),
    path('usuarios/<int:pk>', user_detail_view, name= 'usuario_detail_view')
]