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
from posts.models import Posts

# User = settings.AUTH_USER_MODEL


class NewPostAPIView(APIView):
  def post(self, request):
    request_token = request.data.get('token')
    request_post = request.data.get('post')
    request_file = request.data.get('file')
    token = Token.objects.filter(key=request_token).first()
    user = User.objects.filter(id=token.user_id, is_active=True)
    
    if user.exists() and user.count() == 1:
      user_data = user.first()
      Posts.objects.create(
        user=user_data,
        post=request_post,
        image=request_file
      )
      img = Posts.objects.filter(post=request_post).first().image

      return Response({'message': {'success': True, 'message': 'post saved successfully', 'img': str(img)}}, status=HTTP_200_OK)
    else:
      return Response({'message': {'success': False, 'message': 'post can not be saved successfully'}}, status=HTTP_404_NOT_FOUND)

