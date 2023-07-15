from api.models.branch_store_model import BranchStore
from rest_framework import serializers

class BranchStoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BranchStore
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
