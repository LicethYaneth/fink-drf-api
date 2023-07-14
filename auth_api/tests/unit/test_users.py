from django.test import TestCase
from faker import Faker
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from django.forms.models import model_to_dict
from django.utils.dateparse import parse_datetime

class UserTestCase(TestCase):

    base_url='/users/api/v1/users'
    def setUp(self):
        self.faker = Faker()
        self.client = APIClient()

        for i in range(5):
            user_data={
                'password': self.faker.password(length=10, special_chars=True),
                'last_login': timezone.make_aware(self.faker.date_time_this_month(),timezone.get_current_timezone()),
                'is_superuser': False,
                'username': self.faker.user_name(),
                'first_name': self.faker.first_name(),
                'last_name': self.faker.last_name(),
                'email': self.faker.email(),
                'is_staff': False,
                'is_active': True,
                'date_joined': timezone.make_aware(self.faker.date_time_this_month(),timezone.get_current_timezone()),
            }
            
            User.objects.create(**user_data)

        self.expected_users=User.objects.all()


    def test_users_can_be_queried(self):

        response = self.client.get(self.base_url+'/')
        actual_users = response.json()
        #Verificar que la respuesta tiene un código de estado HTTP 200 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Verificar que los datos de cada usuario coincide con lo esperado
        for actual_user, expected_user in zip(actual_users, self.expected_users):
            actual_user['last_login'] = parse_datetime(actual_user['last_login'])
            actual_user['date_joined'] = parse_datetime(actual_user['date_joined'])

            expected_user_dict = model_to_dict(expected_user)
            self.assertDictEqual(actual_user, expected_user_dict)

    def test_can_get_user_by_id(self):
        expected_user_dict = model_to_dict(self.expected_users[0])
        response = self.client.get(f'{self.base_url}/{str(expected_user_dict["id"])}/')
        actual_user = response.json()
        #Verificar que la respuesta tiene un código de estado HTTP 200 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

        #Verificar que la información del usurio coincide
        actual_user['last_login'] = parse_datetime(actual_user['last_login'])
        actual_user['date_joined'] = parse_datetime(actual_user['date_joined'])
        
        self.assertEqual(actual_user, expected_user_dict)
