from django.db import models

class BranchStore(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.name