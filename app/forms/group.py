from django import forms

from app.models import Group
from crispy_forms.helper import FormHelper

class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ('group_name',)

	group_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Group Name', 'style': 'width:50%'}))

	def __init__(self, *args, **kwargs):
		super(GroupForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()