from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    
    def validate_name(self, value):
        if 'develop' in value:
           raise serializers.ValidationError('El nombre no es un correo aceptado')
         
        return value
    
    def validate_email(self, value): 
        if value == '':
            raise serializers.ValidationError('Tiene que poner un correo valido')
        return value 
    
    def validate(self, data): 
        return data
        
    def create(self, validate_data):
        print(validate_data)
        return User.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.email = validate_data.get('email', instance.email)
        instance.save()
        return instance