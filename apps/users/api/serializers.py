from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
 
 
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name', 'last_name')
          
class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password_two = serializers.CharField(max_length=128, min_length=6, write_only=True)
    
    
    def validate(self, data):
        if data["password"] != data["password_two"]:
            raise serializers.ValidationError({'password':'Debe ingresar ambas contrasena iguales'})
        return data

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
    def to_representation(self, instance):
        return {
            "id": instance["id"],
            "name": instance["name"],
            "email": instance["email"],
            "username": instance["username"],
        }
 
 
 