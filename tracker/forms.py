from django import forms
from tracker.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseForm(forms.ModelForm):
    transaction_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Expense
        fields = ("__all__")
        exclude = ['submitted_by']
