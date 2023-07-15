from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
import base64

class LoginView(APIView):
  authentication_classes = [BasicAuthentication]

  def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      try:
        user = User.objects.get(username=username)
        if user.check_password(password):
          credentials = username + ":" + password
          credentials_bytes = credentials.encode("ascii")
          base64_bytes = base64.b64encode(credentials_bytes)
          base64_string = base64_bytes.decode("ascii")
          return Response(
              data= {
                "message": "Login Succesful!!",
                "access_token": base64_string
              },
              status= status.HTTP_200_OK
          )
      except User.DoesNotExist:
          pass

      return Response( 
        data= {
            "message": "Invalid username or password."
        },
        status=status.HTTP_400_BAD_REQUEST
      )