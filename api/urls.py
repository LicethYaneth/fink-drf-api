from django.urls import path, include
from api.views.branch_store_view import BranchStoreView
from api.views.seller_view import SellerView
from api.views.monthly_record_view import MonthlyRecordView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'branch_stores',BranchStoreView,basename='branch_stores')
router.register(r'sellers',SellerView,basename='sellers')
urlpatterns=[
    path("", include(router.urls)),
    path('balance-monthly/', MonthlyRecordView.as_view(), name='balance-monthly'),
]
