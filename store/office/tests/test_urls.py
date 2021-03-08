from django.test import SimpleTestCase,Client,TestCase
from django.urls import resolve,reverse
from office.views import employeeregister, home, productview, orderview, orderdetailview, employeeapiview, officecodeapi


class TestUrls(TestCase):

    def setUp(self):
        self.c=Client()

    def test_url(self):
        resp = self.c.get("/product/")
        




