from django.test import TestCase
from django.shortcuts import reverse

class LandingPageTest(TestCase):

    def test_get(self):
        # har qanday sinov
        response = self.client.get(reverse("user:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "layout.html")


