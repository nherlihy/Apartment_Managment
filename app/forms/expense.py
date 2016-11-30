from django import forms

from app.models import Expense
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField
from crispy_forms.bootstrap import PrependedText

class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ('description', 'cost', 'pay_to', 'due_by')

	description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Expense Title', 'style': 'width:70%'}))
	cost = forms.DecimalField(label='Cost', widget=forms.NumberInput(attrs={'placeholder': '5.00', 'style': 'width:70%'}))
	pay_to = forms.ModelChoiceField(queryset='', empty_label='Select One')
	due_by = forms.DateField(label='Due Date', widget=forms.SelectDateWidget(attrs={'style': 'width:70%; display: inline-block;'}))

	def __init__(self, *args, **kwargs):
		super(ExpenseForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()

		self.helper.layout = Layout(
		    'description',
		    'cost',
		    'pay_to',
		    MultiWidgetField('due_by', attrs=({'style': 'width: 25%; display: inline-block;'})),
		)