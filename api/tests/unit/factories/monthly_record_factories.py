from faker import Faker
from api.models.branch_store_model import BranchStore
faker = Faker()

class MonthlyRecordFactory:

    def monthly_record_JSON():
      Branch_stores=BranchStore.objects.all()
      return {
        'month' : faker.month_name(),
        'sales' : faker.random_int(min=10000, max=99999),
        'costs' : faker.random_int(min=1000, max=99999),
      }
