from django.urls import path, include
from rest_framework import routers
from auth_api.views.user_view import UserView

router = routers.DefaultRouter()
router.register(r'users',UserView,'users')
urlpatterns=[path("api/v1/", include(router.urls))]