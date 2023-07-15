from api.models.seller_model import Seller
from rest_framework import serializers

class SellerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Seller
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
