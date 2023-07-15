from django.urls import path, include
from rest_framework import routers
from auth_api.views.user_view import UserView
from auth_api.views.login_view import LoginView

router = routers.DefaultRouter()
router.register(r'users',UserView,basename='users')

urlpatterns=[
    path("", include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
