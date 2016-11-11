from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper


# Inherited from the default User Model

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    comfirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Comfirm Password'}))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean(self):
        super(UserForm, self).clean()
        password = self.cleaned_data.get('password')
        comfirm_password = self.cleaned_data.get('comfirm_password')

        if password != comfirm_password:
            raise forms.ValidationError({'password': ["Passwords dont match", ]})

        return self.cleaned_data
