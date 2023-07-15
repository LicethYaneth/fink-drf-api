from django.contrib.auth.models import User
from api.models.branch_store_model import BranchStore
from auth_api.tests.unit.factories.user_factories import UserFactory
from django.utils import timezone
from faker import Faker

faker = Faker()

class SellerFactory:

    def build_seller_JSON():
      branch_stores = BranchStore.objects.all()
      user = User.objects.create(**UserFactory.build_user_JSON())
      birthdate = faker.date_time_between(start_date='-65y', end_date='-18y', tzinfo=timezone.utc).isoformat()
      return {
        'address' : faker.address(),
        'birthdate' : birthdate,
        'branch_store' : faker.random_element(branch_stores),
        'user' : user,
        'is_active' : True
        }
