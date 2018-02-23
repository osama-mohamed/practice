from django.test import TestCase


class TestCalls(TestCase):

    def test_users(self):
        response = self.client.post('',
                                    user_one='OSAMAMOHAMED1234',
                                    user_two='octocat'
                                    )
        self.assertEqual(response.status_code, 200)


    def test_users_api(self):
        response = self.client.post('/api/',
                                    user_one='OSAMAMOHAMED1234',
                                    user_two='octocat'
                                    )
        self.assertEqual(response.status_code, 200)
