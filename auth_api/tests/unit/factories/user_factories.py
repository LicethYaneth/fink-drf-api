from faker import Faker
from django.utils import timezone

faker = Faker()

class UserFactory:

    def build_user_JSON():
        return {
        'password': faker.password(length=10, special_chars=True),
        'last_login': timezone.make_aware(faker.date_time_this_month(),timezone.get_current_timezone()),
        'is_superuser': False,
        'username': faker.user_name(),
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
        'is_staff': False,
        'is_active': True,
        'date_joined': timezone.make_aware(faker.date_time_this_month(),timezone.get_current_timezone()),
        }

    def build_login_JSON(user):
        return {
            "username": user["username"],
            "password": user["password"]
        }
    
    def build_login_fake_JSON():
        return {
            'username': faker.user_name(),
            'password': faker.password(length=10, special_chars=True),
        }