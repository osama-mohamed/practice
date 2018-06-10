from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
# from rest_framework.authtoken.models import Token

# from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Account


# User = settings.AUTH_USER_MODEL

class CheckUsernameAPIView(APIView):
  def post(self, request):
    try:
      qs = User.objects.filter(username=request.data['username'], is_active=True)
      if qs:
        return Response({'message': {'success': True}}, status=HTTP_200_OK)
      else:
        return Response({'message': {'success': 'not found'}}, status=HTTP_200_OK)
    except:
      return Response({'message': {'success': False}}, status=HTTP_400_BAD_REQUEST)


class SignUpAPIView(APIView):
  def post(self, request):
    try:
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
      return Response({'message': {'success': True}}, status=HTTP_200_OK)
    except:
      return Response({'message': {'success': False}}, status=HTTP_400_BAD_REQUEST)


class SignInAPIView(APIView):
  def post(self, request):
    try:
      user = User.objects.filter(username=request.data['username'], is_active=True)
      if user.exists() and user.count() == 1:
        user_data = user.first()
        username = request.data['username']
        password = request.data['password']
        print(user_data.password)
        print(password)
        # token = Token.objects.create(user=request)
        # print(token)

        if username and password:
          c = check_password(password, user_data.password)
          if check_password(password, user_data.password) == True:
            # user = authenticate(username=username, password=password)
            return Response({'message': {'success': True, 'message': 'logged in successfully', 'token': 'random token is here for test'}}, status=HTTP_200_OK)
          else:
            return Response({'message':  {'success': False, 'message': 'invalid password'}}, status=HTTP_200_OK)
      else:
        return Response({'message': {'success': False, 'message': 'user not found'}}, status=HTTP_200_OK)
    except:
      return Response({'message': {'success': False}}, status=HTTP_400_BAD_REQUEST)
