from django.urls import path, include
from api.views.branch_store_view import BranchStoreView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'branch_stores',BranchStoreView,basename='branch_stores')
urlpatterns=[path("", include(router.urls))]
