from django.test import TestCase, Client
class GreetingsViewsTest(TestCase):

    def test_greetings(self):
        
        response = self.client.get("/greetings/radek")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello Radek !', response.content.decode())
