from django.test import TestCase
from django.urls import reverse


class TwoSumTest(TestCase):

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_two_sum(self):
        response = self.client.post(
            reverse("two_sum"),
            {
                "num1": 10,
                "num2": 20
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["result"], 30)