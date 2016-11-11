from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper

class LoginForm(forms.Form):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Username'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()