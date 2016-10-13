from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Username'}))
	email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
