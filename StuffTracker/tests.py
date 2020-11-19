from django.test import TestCase, Client
from .models import Stuff
import unittest
# Create your tests here.
class StuffStrTest(TestCase):
    def test_matchName(self):
        name = "Thomas"
        n = Stuff(name = name)
        self.assertEqual(name,str(n))

    # def setUp(self):
    #     # Every test needs a client.
    #     self.client = Client()
    #
    # def test_details(self):
    #     # Issue a GET request.
    #     response = self.client.get('/customer/details/')
    #
    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Check that the rendered context contains 5 customers.
    #     self.assertEqual(len(response.context['customers']), 5)
    def setUp(self):
        c = Client()
        r = c.post("/login/", {"name": "noman", "password": "1234"})
        self.assertEqual("noman", r.context["name"])

    def test_details(self):
        client = Client()
        response = client.get('/things/')
        self.assertEqual(response.status_code, 200)

    def test_something(self):
        session = self.client.session

        session['somekey'] = 'test'

        session.save()


suite = unittest.defaultTestLoader.loadTestsFromTestCase(StuffStrTest)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDiv)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMul)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSub)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestEqual)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestFloat)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(testStr)
unittest.TextTestRunner().run(suite)