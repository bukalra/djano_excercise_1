from maths.forms import ResultForm
from django.test import TestCase

# Create your tests here.
from maths.models import Math, Result


class ResultFormTest(TestCase):

    def test_result_save_correct_data(self):
        data = {"value": 200}
        self.assertEqual(len(Result.objects.all()), 0)
        form = ResultForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Result)
        self.assertEqual(r.value, 200)
        self.assertIsNotNone(r.id)
        self.assertIsNone(r.error)