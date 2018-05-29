from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Account


# User = settings.AUTH_USER_MODEL

class SignInAPIView(APIView):
  def post(self, request):
    # try:
      user = User(
        first_name = request.data['firstName'],
        last_name = request.data['lastName'],
        username = request.data['username'],
        email = request.data['email'],
      )
      user.set_password(request.data['password'])
      user.is_active = False
      user.save()
      newAccount = Account(
        gender = request.data['gender'],
        user= user
      )
      newAccount.save()
      return Response({'message': ['Success!']}, status=HTTP_200_OK)
    # except:
    #   return Response({'message': ['Failled!']}, status=HTTP_400_BAD_REQUEST)
