from api.models.seller_model import Seller
from rest_framework import serializers
from api.serializers.branch_store_serializer import BranchStoreSerializer
from auth_api.serializers.user_serializer import UserSerializer
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
