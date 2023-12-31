from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.models.monthly_record_model import MonthlyRecord
from api.utils.user_util import UserUtil

class MonthlyRecordView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try: 
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            auth_type, token = authorization_header.split(' ')
            data = request.data
            anual_balance = []
            for i in range(len(data['Mes'])):
                month = data['Mes'][i]
                sales = data['Ventas'][i]
                costs = data['Gastos'][i]
                balance = sales - costs
                user = UserUtil.get_user_info(token)
                branch = UserUtil.get_branch(user)
                if branch["error"] is True:
                    if branch["detail"] == "branch":
                        return Response(
                            data= {
                                "message": "No se encontro la sucursal"
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    if branch["detail"] is "seller":
                        return Response(
                            data= {
                                "message": "El usuario no esta asociado a un vendedor"
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
                MonthlyRecord.objects.create(
                    month=month,
                    sales=sales,
                    costs=costs,
                    balance=balance,
                    user=user,
                    branch=branch["branch"]
                )
                monthly_balance = {
                    'mes': month,
                    'Ventas': sales,
                    'Gastos': costs,
                    'Balance': balance
                }
                anual_balance.append(monthly_balance)
            return Response(
                data={
                    'anual_balance': anual_balance
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                data={
                    "message": "Error en el servicio"
                },
                status=status.HTTP_400_BAD_REQUEST
            )