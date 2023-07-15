from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.models.monthly_record_model import MonthlyRecord
from api.utils.user_util import UserUtil

class SortedNumberView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        unsorted_numbers = request.data.get("sin_clasificar")
        if unsorted_numbers is None or len(unsorted_numbers) <= 0:
            return Response(
                data={
                    "Message": "La lista es nula"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        non_duplicates = []
        duplicates = []
    
        for element in unsorted_numbers:
            if element not in non_duplicates:
                non_duplicates.append(element)
            else:
                duplicates.append(element)
    
        sorted_list = sorted(non_duplicates) + sorted(duplicates)
        return Response(
            data={
                'sin clasificar': unsorted_numbers,
                "clasificado": sorted_list
            },
            status=status.HTTP_200_OK
        )