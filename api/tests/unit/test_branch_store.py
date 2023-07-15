from django.test import TestCase
from api.models.branch_store_model import BranchStore
from rest_framework.test import APIClient
from rest_framework import status
from django.forms.models import model_to_dict
from django.utils.dateparse import parse_datetime
from api.tests.unit.factories.branch_store_factories import BranchStoreFactory

class BranchStoreTestCase(TestCase):

    base_url='/api/branch_stores'
    def setUp(self):
        self.client = APIClient()

        for i in range(5):
            BranchStore.objects.create(**BranchStoreFactory.build_branch_store_JSON())

        self.expected_branch_stores=BranchStore.objects.all()

    def test_branch_stores_can_be_queried(self):

        response = self.client.get(self.base_url+'/')
        actual_branch_stores = response.json()
        #Verificar que la respuesta tiene un código de estado HTTP 200 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Verificar que los datos de cada sucursal coincida con lo esperado
        for actual_branch_store, expected_branch_store in zip(actual_branch_stores, self.expected_branch_stores):
            expected_branch_store_dict = model_to_dict(expected_branch_store)
            
            self.assertEqual(expected_branch_store_dict['name'],actual_branch_store['name'])
            self.assertEqual(expected_branch_store_dict['address'],actual_branch_store['address'])

    def test_can_get_branch_store_by_id(self):
        expected_branch_store_dict = model_to_dict(self.expected_branch_stores[0])
        response = self.client.get(f'{self.base_url}/{str(expected_branch_store_dict["id"])}/')
        actual_branch_store = response.json()      

        #Verificar que la respuesta tiene un código de estado HTTP 200 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #Verificar que la información de la sucursal coincide
        self.assertEqual(actual_branch_store['name'], expected_branch_store_dict['name'])
        self.assertEqual(actual_branch_store['address'], expected_branch_store_dict['address'])


    def test_branch_store_can_be_created(self):
        branch_store = BranchStoreFactory.build_branch_store_JSON()
        response= self.client.post(self.base_url+'/',branch_store,format='json')
        actual_branch_store = response.json()

        #Verificar que la respuesta tiene un código de estado HTTP 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #Verificar que la información de la sucursla coincide con el creado
        self.assertEqual(actual_branch_store['name'], branch_store['name'])
