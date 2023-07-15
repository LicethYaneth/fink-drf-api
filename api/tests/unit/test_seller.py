from django.test import TestCase
from api.models.seller_model import Seller
from django.contrib.auth.models import User
from api.models.branch_store_model import BranchStore
from rest_framework.test import APIClient
from rest_framework import status
from django.forms.models import model_to_dict
from django.utils.dateparse import parse_datetime
from api.tests.unit.factories.seller_factories import SellerFactory
from api.tests.unit.factories.branch_store_factories import BranchStoreFactory
from auth_api.tests.unit.factories.user_factories import UserFactory

class SellerTestCase(TestCase):

    end_point_sellers='/api/sellers'
    def setUp(self):
        self.client = APIClient()
        for i in range(1):
            BranchStore.objects.create(**BranchStoreFactory.build_branch_store_JSON())
            User.objects.create(**UserFactory.build_user_JSON())
            Seller.objects.create(**SellerFactory.build_seller_JSON())

        self.expected_sellers=Seller.objects.all()
    
    def test_sellers_can_be_queried(self):

        response = self.client.get(self.end_point_sellers+'/')
        actual_sellers = response.json()
        #Verificar que la respuesta tiene un código de estado HTTP 200 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Verificar que los datos de cada vendedor coincide con lo esperado
        for actual_seller, expected_seller in zip(actual_sellers, self.expected_sellers):

            expected_seller_dict = model_to_dict(expected_seller)
            self.assertEqual(expected_seller.user_id, actual_seller['user'])
            self.assertEqual(expected_seller.branch_store_id, actual_seller['branch_store'])

    def test_can_get_seller_by_id(self):
        expected_seller_dict = model_to_dict(self.expected_sellers[0])
        response = self.client.get(f'{self.end_point_sellers}/{str(expected_seller_dict["id"])}/')
        actual_seller = response.json()

        #Verificar que la respuesta tiene un código de estado HTTP 200 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #Verificar que la información del vendedor coincide
        self.assertEqual(expected_seller_dict["user"], actual_seller['user'])
        self.assertEqual(expected_seller_dict["branch_store"], actual_seller['branch_store'])

