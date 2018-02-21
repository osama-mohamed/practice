from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

import requests

URL = 'https://api.github.com/users/{}'


class UserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_data = serializer.data
            user_name_one = new_data.get('user_name_one')
            user_name_two = new_data.get('user_name_two')
            try:
                user_one_result = requests.get(URL.format(user_name_one)).json()
                user_two_result = requests.get(URL.format(user_name_two)).json()
                if user_one_result.get('message') == 'Not Found' or user_two_result.get('message') == 'Not Found':
                    return Response({'message': 'We could not found these users!'})
                else:
                    return Response({'user_one_stats': user_one_result,
                                     'user_two_stats': user_two_result})
            except:
                return Response({'message': 'There is unexpected error'})
        return Response({'message': 'Type anything to show results'})
