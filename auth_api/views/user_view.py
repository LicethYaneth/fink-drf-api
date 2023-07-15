from rest_framework import viewsets
from auth_api.serializers.user_serializer import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):
        if 'password' in serializer.validated_data:
            password = make_password(serializer.validated_data['password'])
            serializer.save(password=password)
        else:
            serializer.save()
