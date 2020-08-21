from django import forms
from tracker.models import *

from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseForm(forms.ModelForm):
    transaction_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Expense
        fields = ("__all__")
        exclude = ['submitted_by', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        amount = cleaned_data.get('amount')

        if category.name == 'travel' and amount > 7500:
            raise forms.ValidationError(
                "Value cannot be more than 7500 for Category 'Travel'")
        elif category.name == 'misc' and amount > 1500:
            raise forms.ValidationError(
                "value cannot be more than 1500 for Category 'Misc'")
        # self.add_error()
