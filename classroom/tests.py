from django.test import TestCase, Client
from django.urls import reverse


class LoginPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page_returns_correct_html(self):
        login_url = reverse('login')
        response = self.client.get(login_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username', response.content)
        self.assertIn(b'Password', response.content)

        registration_url = reverse('registration')
        response = self.client.post(registration_url)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'This field is required.', response.content)

        response = self.client.post(login_url, {'username': 'bad', 'password': 'bad'})
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Please enter a correct username and password.', response.content)

    def test_login_as_teacher(self):
        login_url = reverse('login')
        response = self.client.post(login_url, {'username': 'sumee', 'password': 'sdsdsd1910'}, follow=True)
        if response.redirect_chain:
            self.assertEqual(response.redirect_chain[0][0], reverse('teachers:quiz_change_list'))
        else:
            self.fail("Redirection failed")
