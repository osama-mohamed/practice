from django.test import TestCase
from django.core.urlresolvers import reverse


class TestCalls(TestCase):

    def test_users(self):
        response = self.client.post(reverse('github_detail:home'),
                                    user_name_one='OSAMAMOHAMED1234',
                                    user_name_two='octocat'
                                    )
        self.assertEqual(response.status_code, 200)
        # print(response.content)
        # print('***************')
        # print(response.context['login'])
        # print('------------------------')
        # print(response.data)
        # print(response.context['user_one'])
        # print(response.context)


    def test_users_api(self):
        response = self.client.post(reverse('github_detail_api:home_api'), {
                                    'user_name_one': 'OSAMAMOHAMED1234',
                                    'user_name_two': 'octocat'}
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['user_one_stats']), 30)
        self.assertEqual(response.json()['user_one_stats']['login'], 'OSAMAMOHAMED1234')
        self.assertEqual(len(response.json()['user_one_stats']['login']), 16)
        self.assertEqual(len(response.json()), 2)
