from faker import Faker
faker = Faker()

class BranchStoreFactory:

    def build_branch_store_JSON():
        return {
        'name': faker.company_suffix(),
        'address': faker.address(),
        }
