from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

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
      username = request.data['username']
      password = request.data['password']
      user = User.objects.filter(username=username, is_active=True)
      if user.exists() and user.count() == 1:
        user_data = user.first()
        Token.objects.filter(user_id=user_data.id).delete()
        token = Token.objects.get_or_create(user_id=user_data.id)

        if username and password:
          c = check_password(password, user_data.password)
          if check_password(password, user_data.password) == True:
            user = authenticate(username=username, password=password)
            login(request, user)
            return Response({'message': {'success': True, 'message': 'logged in successfully'}, 'user': {'token': str(token[0])}}, status=HTTP_200_OK)
          else:
            return Response({'message':  {'success': False, 'message': 'invalid password'}}, status=HTTP_200_OK)
      else:
        return Response({'message': {'success': False, 'message': 'user not found'}}, status=HTTP_200_OK)
    except:
      return Response({'message': {'success': False}}, status=HTTP_400_BAD_REQUEST)


class SignOutAPIView(APIView):
  def post(self, request):
    token = request.data['token']
    user = Token.objects.filter(key=token)
    if user.exists() and user.count() == 1:
      user_data = user.first()
      user_data.delete()
      logout(request)
      return Response({'message': {'success': True, 'message': 'logged out successfully'}}, status=HTTP_200_OK)
    else:
      return Response({'message': {'success': False, 'message': 'user not found'}}, status=HTTP_200_OK)



class ProfileAPIView(APIView):
  def post(self, request, *args, **kwargs):
    request_token = request.data.get('token')
    token = Token.objects.filter(key=request_token).first()
    user = User.objects.filter(id=token.user_id, is_active=True)
    
    # print(request.headers['Authorization'])
    if user.exists() and user.count() == 1:
      user_data = user.first()
      current_user = {
        'id': user_data.id,
        'username': user_data.username,
        'token': str(token)
      }
      return Response({'message': {'success': True}, 'user': current_user}, status=HTTP_200_OK)
    else:
      return Response({'message': {'success': False, 'message': 'user not found'}}, status=HTTP_404_NOT_FOUND)

