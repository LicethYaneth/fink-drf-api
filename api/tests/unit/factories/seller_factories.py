from django.contrib.auth.models import User
from api.models.branch_store_model import BranchStore
from auth_api.tests.unit.factories.user_factories import UserFactory
from django.utils import timezone
from faker import Faker
from django.forms.models import model_to_dict
from api.tests.unit.factories.branch_store_factories import BranchStoreFactory
import json


faker = Faker()

class SellerFactory:

    def build_seller_JSON():
      branch_store = BranchStore.objects.create(**BranchStoreFactory.build_branch_store_JSON())
      user = User.objects.create(**UserFactory.build_user_JSON())
      birthdate = faker.date_time_between(start_date='-65y', end_date='-18y', tzinfo=timezone.utc).isoformat()
      return {
        'address' : faker.address(),
        'birthdate' : birthdate,
        'branch_store' : branch_store,
        'user' : user,
        'is_active' : True
        }
