from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer, UpdateUserSerializer, PasswordSerializer

class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.object\
                .filter(is_active = True)\
                .values('id','username','email', 'name')
        return self.queryset
    
    def get_object(self, pk=None):
        return get_object_or_404(self.serializer_class().Meta.model, pk=pk)
    
    def list(self, request):
        users = self.queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["POST"], url_path="SetPass")
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        pass_serializer = PasswordSerializer(data=request.data)
        if pass_serializer.is_valid():
            user.set_password(pass_serializer.validate_data.get('password', ''))
            user.save()      
            return Response({
                    "message": "Contrasena actualizada correctamente"
                })
        return Response({
                    "message": "Hay errores en la informacion enviada"
           }, status=status.HTTP_400_BAD_REQUEST)   
    
    def create(self, request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message": "Usuario creado correctamente."}, status=status.HTTP_200_OK)
        return Response({"message": "Hay errores en el registro", "errors": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            return Response({
                "message":"Usuario actualizado correctamente"
            }, status =status.HTTP_200_OK)
            
        return Response({"message":"Hay errores en la actualizacion", "errors": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = self.get_object(pk)
        user_destroy = self.serializer_class(user).update(is_active=False)
        if user_destroy == 1:
            return Response({
                    "message":"Usuario eliminado correctamente"
                })
        return Response({"message":"No existe el usuario que desea eliminar"}, status=status.HTTP_404_NOT_FOUND)