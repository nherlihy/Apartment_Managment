from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper

class JoinGroupForm(forms.Form):
	groupname = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Group Name'}))

def __init__(self, *args, **kwargs):
		super(GroupForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()  