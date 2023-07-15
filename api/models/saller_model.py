from django.db import models
from django.contrib.auth.models import User
from api.models.branch_store_model import BranchStore


class Seller(models.Model):
    address = models.CharField(max_length=200)
    birthdate = models.DateTimeField()
    branch_store = models.ForeignKey(BranchStore)
    user = models.OneToOneField(User)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)