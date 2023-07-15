from django.db import models
from django.contrib.auth.models import User
from api.models.branch_store_model import BranchStore

class MontlyRecord(models.Model):
    month = models.CharField(max_length=50)
    sales = models.CharField(max_length=100)
    costs = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    branch = models.ForeignKey(BranchStore, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)