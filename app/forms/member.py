from django import forms

from app.models import Member
from crispy_forms.helper import FormHelper

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('username', 'email', 'password')