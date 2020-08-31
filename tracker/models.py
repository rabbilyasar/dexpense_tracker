from django.db import models
# from django.contrib.auth.models import User
from account.models import Account
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError


def validate_date(date):
    current_date = datetime.today().date()
    if date < current_date-timedelta(days=30):
        raise ValidationError("Date cannot be less than 30 days from now")
    elif date > current_date:
        raise ValidationError("Date cannot be greater than current day")


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Expense(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    submitted_by = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    amount = models.IntegerField(default=1,
                                 validators=[
                                     MaxValueValidator(10000),
                                     MinValueValidator(1)
                                 ])
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    transaction_date = models.DateField(null=True, validators=[validate_date])
    image = models.ImageField(upload_to='image', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("change_expense_status", "Can change the status of expense"),
            ("can_view_approve_expense", "Can view approved expenses"),
        ]

    def __str__(self) -> str:
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
