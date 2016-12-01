from django import forms

from app.models import Expense, Member
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField
from crispy_forms.bootstrap import PrependedText

class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ('description', 'total_cost', 'pay_to', 'due_by')

	description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Expense Title', 'style': 'width:70%'}))
	total_cost = forms.DecimalField(label='Total Cost', widget=forms.NumberInput(attrs={'placeholder': '5.00', 'style': 'width:70%'}))
	pay_to = forms.ModelChoiceField(queryset=Member.objects.all(), empty_label='Select One')
	due_by = forms.DateField(label='Due Date', widget=forms.SelectDateWidget(attrs={'style': 'width:70%; display: inline-block;'}))

	def __init__(self, *args, **kwargs):
		super(ExpenseForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()

		self.helper.layout = Layout(
		    'description',
		    'total_cost',
		    'pay_to',
		    MultiWidgetField('due_by', attrs=({'style': 'width: 25%; display: inline-block;'})),
		)

	def clean(self):
		cleaned_data = self.cleaned_data
		if cleaned_data.get('total_cost'):
			cleaned_data['total_cost'] = '{0:.2f}'.format(cleaned_data['total_cost']) #Format cost to the 2nd decimal place

		return cleaned_data