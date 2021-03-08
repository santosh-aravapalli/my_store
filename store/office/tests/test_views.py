from django.test import TestCase,Client
from office.views import *
from django.urls import reverse


class test_views(TestCase):

    def setup(self):
        self.client = Client()


    def test_office_view(self):
        resp = Client().get(reverse("products"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,"home.html")

