from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tracker.views import *


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('tracker:home')
        self.assertEquals(resolve(url).func, home)

    def test_login_url_is_resolved(self):
        url = reverse('tracker:login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_register_url_is_resolved(self):
        url = reverse('tracker:register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_logout_url_is_resolved(self):
        url = reverse('tracker:logout')
        self.assertEquals(resolve(url).func, logoutPage)

    def test_approved_expense_url_is_resolved(self):
        url = reverse('tracker:approved_expense')
        self.assertEquals(resolve(url).func, approvedExpenses)

    def test_create_expense_url_is_resolved(self):
        url = reverse('tracker:create_expense')
        self.assertEquals(resolve(url).func, createExpense)

    def test_update_expense_url_is_resolved(self):
        url = reverse('tracker:update_expense', args=["str"])
        self.assertEquals(resolve(url).func, updateExpense)

    def test_delete_expense_url_is_resolved(self):
        url = reverse('tracker:delete_expense', args=["str"])
        self.assertEquals(resolve(url).func, deleteExpense)

    def test_change_status_url_is_resolved(self):
        url = reverse('tracker:change_status', args=["str"])
        self.assertEquals(resolve(url).func, changeStatus)
