# from django.test import TestCase, Client
# from django.urls import reverse
# from tracker.models import Expense
# import json


# class TestViews(TestCase):

#     def test_expense_home_GET(self):
#         client = Client()

#         response = client.get(reverse('tracker:home'))

#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'tracker/home.html')
