import django_filters
from django_filters import DateFilter

from django import forms

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="transaction_date", lookup_expr='gte')
    end_date = DateFilter(field_name="transaction_date", lookup_expr='lte')

    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['image', 'description', 'date_created',
                   'amount', 'transaction_date', 'title']
        # widgets = {
        #     'transaction_date': forms.DateField(attrs={'type': 'date'})
        # }
