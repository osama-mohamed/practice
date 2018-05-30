from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.db.models import Q

# from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Account


# User = settings.AUTH_USER_MODEL

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
      user = User.objects.filter(
        Q(username=request.data['username'], is_active=True) |
        Q(email=request.data['email'], is_active=True)
      ).distinct()
      print(user)
      user = user.exclude(email__isnull=True).exclude(email__iexact='')
      if user.exists() and user.count() == 1:
        user_data = user.first()
        print(user_data)
        return Response({'message': {'success': True}}, status=HTTP_200_OK)
      else:
        return Response({'message': {'success': 'not found'}}, status=HTTP_200_OK)
    except:
      return Response({'message': {'success': False}}, status=HTTP_400_BAD_REQUEST)
