from app.models.models import Expense
from django import forms

from crispy_forms.helper import FormHelper


class ExpenseForm(forms.Form):
    expense_cost = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Cost'}))
    expense_pay_to = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Pay To'}))

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
