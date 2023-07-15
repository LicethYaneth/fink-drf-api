from django.test import TestCase
from rest_framework.test import APIClient
from auth_api.tests.unit.factories.user_factories import UserFactory
from rest_framework import status

class LoginTestCase(TestCase):
    
    endpoint_login = '/api/auth/login'
    endpoint_users ='/api/auth/users'
    user_created = {}

    def setUp(self):
      self.client = APIClient()

      self.user_created = UserFactory.build_user_JSON()
      response= self.client.post(self.endpoint_users+'/',self.user_created,format='json')

    def test_login_successful(self):
      request = UserFactory.build_login_JSON(self.user_created)
      responseLogin = self.client.post(self.endpoint_login+'/',request,format='json')
      token = responseLogin.data['access_token']
      self.assertIsNotNone(token)

    def test_login_unsuccessful(self):
        data = UserFactory.build_login_fake_JSON()
        response = self.client.post(self.endpoint_login+'/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        message = response.data['message']
        self.assertEqual(message, 'Invalid username or password.')