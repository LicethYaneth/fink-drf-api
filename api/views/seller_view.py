from rest_framework import viewsets
from api.serializers.seller_serializer import SellerSerializer
from api.models.seller_model import Seller

class SellerView(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()