from rest_framework.test import APITestCase
from rest_framework import status


from faker import Faker

class TestSetup(APITestCase):
    
    def setUp(self):     
        from apps.users.models import User
        
        faker = Faker()
        
        self.login_url = '/login/'
        self.user = User.objects.create_superuser(
            name="developer",
            last_name="dev",
            username= faker.name(),
            password="123456",
            email=faker.email()
        )
        
        response = self.client.post(
            self.login_url, 
            {
                "username": self.user.username,
                "password": "123456"
            },
            format= 'json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.token = response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+ self.token)
        return super().setUp()
    