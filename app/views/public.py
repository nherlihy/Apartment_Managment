from django.shortcuts import render

from app.forms.user_registration import UserForm

def home(request):
	user_form = UserForm()
	return render(request, 'public/home.html', {'user_form' : user_form})