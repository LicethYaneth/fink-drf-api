from django.test import TestCase
from faker import Faker
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from django.forms.models import model_to_dict
from django.utils.dateparse import parse_datetime
from auth_api.tests.unit.factories.user_factories import UserFactory
class UserTestCase(TestCase):

    base_url='/users/api/v1/users'
    def setUp(self):
        self.client = APIClient()

        for i in range(5):
            User.objects.create(**UserFactory.build_user_JSON())

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
        actual_user['last_login'] = parse_datetime(actual_user['last_login'])
        actual_user['date_joined'] = parse_datetime(actual_user['date_joined'])
        

        #Verificar que la respuesta tiene un código de estado HTTP 200 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #Verificar que la información del usurio coincide
        self.assertEqual(actual_user, expected_user_dict)

    def test_can_be_created(self):
        user = UserFactory.build_user_JSON()
        response= self.client.post(self.base_url+'/',user,format='json')
        actual_user = response.json()
        actual_user['last_login'] = parse_datetime(actual_user['last_login'])
        actual_user['date_joined'] = parse_datetime(actual_user['date_joined'])

        #Verificar que la respuesta tiene un código de estado HTTP 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #Verificar que la información del usurio coincide con el creado
        self.assertEqual(actual_user['username'], user['username'])

