from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UrlSerializer

import requests
import json

API_KEY = 'AIzaSyBQt54uGw2lsD22LLgyiiHnL9M9IjB8BIg'
URL = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format(API_KEY)


class UrlAPIView(APIView):
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            new_data = serializer.data
            url = new_data.get('url')
            long_url = {'longUrl': url}
            headers = {'content-type': 'application/json'}
            response = requests.post(URL, data=json.dumps(long_url), headers=headers).json()
            try:
                return Response({'Short URL : ': response['id'],
                                 'Long URL : ': response['longUrl']})
            except:
                return Response({'message': 'There is unexpected error'})
        return Response({'message': 'Type anything to show results'})
