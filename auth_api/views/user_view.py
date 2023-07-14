from rest_framework import viewsets
from auth_api.serializers.user_serializer import UserSerializer
from django.contrib.auth.models import User

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()