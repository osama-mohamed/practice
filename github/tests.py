from django.test import TestCase
from .api.serializers import UserSerializer

# data = urlencode({"something": "something"})
# response = self.client.post("/my/form/", data, content_type="application/x-www-form-urlencoded")

class TestCalls(TestCase):

    def test_users(self):
        response = self.client.post('',
                                    user_one='OSAMAMOHAMED1234',
                                    user_two='octocat'
                                    )
        self.assertEqual(response.status_code, 200)


    def test_users_api(self):
        response = self.client.post('/api/', {
                                    'user_name_one': 'OSAMAMOHAMED1234',
                                    'user_name_two': 'octocat'}
                                    )
        self.assertEqual(response.status_code, 200)
        # print(len(response.json()['user_one_stats']))
        # print(len(response.json()['user_one_stats']['login']))
        # print(response.json()['user_one_stats'])
        # print(response.json()['user_one_stats']['login'])
        self.assertEqual(len(response.json()['user_one_stats']), 30)
        self.assertEqual(response.json()['user_one_stats']['login'], 'OSAMAMOHAMED1234')
        # print(response.content)
        # print(response.context['user_one_stats'])
        # print(response.json()['user_one_stats'])
        # print(response.data)
        # print(response)

