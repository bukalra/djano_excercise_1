from django.test import TestCase, Client
from maths.models import Math, Result
class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        Math.objects.create(operation="add", a=10, b=10)
        Math.objects.create(operation="mul", a=40, b=30)
        Math.objects.create(operation="div", a=60, b=30)

        self.client = Client()

    def test_maths_list(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 4)
        print(f'=================={response.context}')
        print(f'=================={response.context["maths"]}')
        print(f'=================={len(response.context["maths"])}')

        self.assertIn('<li><a href="/maths/histories/1">id:1, a=20, b=30, op=sub</a></li>', response.content.decode())
        self.assertIn('<li><a href="/maths/histories/2">id:2, a=10, b=10, op=add</a></li>', response.content.decode())
        self.assertIn('<li><a href="/maths/histories/3">id:3, a=40, b=30, op=mul</a></li>', response.content.decode())
        self.assertIn('<li><a href="/maths/histories/4">id:4, a=60, b=30, op=div</a></li>', response.content.decode())