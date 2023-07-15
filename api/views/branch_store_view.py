from rest_framework import viewsets
from api.serializers.branch_store_serializer import BranchStoreSerializer
from api.models.branch_store_model import BranchStore

class BranchStoreView(viewsets.ModelViewSet):
    serializer_class = BranchStoreSerializer
    queryset = BranchStore.objects.all()