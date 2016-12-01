from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper


# Inherited from the default User Model

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    username = forms.CharField(required=False, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(required=False, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=False, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required=False, label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=False, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    comfirm_password = forms.CharField(required=False, label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}))

    def __init__(self, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean(self):
        super(UpdateProfile, self).clean()
        password = self.cleaned_data.get('password')
        comfirm_password = self.cleaned_data.get('comfirm_password')

        if password != comfirm_password:
            raise forms.ValidationError({'password': ["Passwords dont match", ]})

        return self.cleaned_data