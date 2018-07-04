from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from django.conf import settings
import os
from django.contrib.auth.models import User
from accounts.models import Account
from posts.models import Posts

from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)

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
      username = user_data.username
      Posts.objects.create(
        user=user_data,
        post=request_post,
        image=request_file
      )
      img = Posts.objects.filter(post=request_post).first().image

      return Response({'message': {'success': True, 'message': 'post saved successfully', 'img': str(img)},
                       'user': {'username': username}}, status=HTTP_200_OK)
    else:
      return Response({'message': {'success': False, 'message': 'post can not be saved successfully'}}, status=HTTP_404_NOT_FOUND)


class ProfilePostsAPIView(APIView):
  def post(self, request):
    request_token = request.data.get('token')
    token = Token.objects.filter(key=request_token)
    
    if token.exists() and token.count() == 1:
      user_id = token.first().user_id
      qs = Posts.objects.filter(user_id=user_id).order_by('-id')
      posts = []
      for post in qs:
        all_posts = {
          "id": post.id,
          "post": post.post,
          "image": str(post.image),
          "added": post.added,
          "updated": post.updated
        }
        posts.append(all_posts)
        
      return Response({'message': {'success': True, 'message': 'posts retrives successfully'}, 
                       'user': {'posts': posts}}, status=HTTP_200_OK)
    else:
      return Response({'message': {'success': False, 'message': 'posts does not retives successfully'}}, status=HTTP_404_NOT_FOUND)


class ProfilePostsForUsernameAPIView(APIView):
  def post(self, request):
    username = request.data.get('username')
    if username:
      qs = Posts.objects.filter(user_id__username=username, publish=True).order_by('-id')
      posts = []
      for post in qs:
        all_posts = {
          "id": post.id,
          "post": post.post,
          "image": str(post.image),
          "added": post.added,
          "updated": post.updated
        }
        posts.append(all_posts)
      user_profile_pic = Account.objects.filter(user_id__username=username).first()
        
      return Response({'message': {'success': True, 'message': 'posts retrives successfully'}, 
                       'user': {'username': username, 'posts': posts, 'userProfilePic': str(user_profile_pic.image)}}, status=HTTP_200_OK)
    else:
      return Response({'message': {'success': False, 'message': 'posts does not retives successfully'}}, status=HTTP_404_NOT_FOUND)



class DeleteProfilePostAPIView(APIView):
  def post(self, request):
    request_id = request.data.get('id')
    if request_id:
      qs = Posts.objects.filter(id=request_id, publish=True).first()
      qs.delete()
      return Response({'message': {'success': True, 'message': 'post deleted successfully'}}, status=HTTP_200_OK)
    else:
      return Response({'message': {'success': False, 'message': 'post does not deleted successfully'}}, status=HTTP_404_NOT_FOUND)
