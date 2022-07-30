from django.test import TestCase
from maths.models import Math, Result

class ResultModelTest(TestCase):

    def setUp(self):
        Result.objects.create(value=10)
        Result.objects.create(error="0 division error!")

    def test_result_str(self):
        r1 = Result.objects.get(value=10)
        r2 = Result.objects.get(error="0 division error!")

        self.assertEqual(str(r1), 'value: 10.0 | error: None')
        self.assertEqual(str(r2), 'value: None | error: 0 division error!')

class MathModelTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        Math.objects.create(operation="add", a=10, b=10)
        Math.objects.create(operation="mul", a=40, b=30)
        Math.objects.create(operation="div", a=60, b=30)        

    def test_result_str(self):
        o1 = Math.objects.get(operation='sub')
        o2 = Math.objects.get(operation='add')
        o3 = Math.objects.get(operation='mul')
        o4 = Math.objects.get(operation='div')

        self.assertEqual(str(o1), 'id:1, a=20, b=30, op=sub')
        self.assertEqual(str(o2), 'id:2, a=10, b=10, op=add')
        self.assertEqual(str(o3), 'id:3, a=40, b=30, op=mul')
        self.assertEqual(str(o4), 'id:4, a=60, b=30, op=div')

