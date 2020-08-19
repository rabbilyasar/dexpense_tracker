from django.db import models
from django.contrib.auth.models import User


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
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    transaction_date = models.DateField(null=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
