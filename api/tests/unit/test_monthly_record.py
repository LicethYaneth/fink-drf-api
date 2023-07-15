from django.test import TestCase
from api.models.monthly_record_model import MonthlyRecord
from rest_framework.test import APIClient
from rest_framework import status
from django.forms.models import model_to_dict
from django.utils.dateparse import parse_datetime
from api.tests.unit.factories.monthly_record_factories import MonthlyRecordFactory

class MonthlyRecordTestCase(TestCase):
    base_url='/api/branch_stores'
    def setUp(self):
      self.client = APIClient()

      for i in range(5):
        MonthlyRecord.objects.create(**MonthlyRecordFactory.build_branch_store_JSON())

      self.expected_branch_stores=MonthlyRecord.objects.all()
