import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse

from app.forms.user_registration import UserForm

def home(request):
	if request.method == 'POST':
		response = {}
		data = {}
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request, user)

			data['url'] = "http://%s" % request.get_host()
			response['data'] = data
			response['success'] = 'success'

		else:
			errors = user_form.errors.as_json()
			data['errors'] = errors
			response['data'] = data
			response['failed'] = 'failed'

		return HttpResponse(json.dumps(response), content_type='application/json')

	elif request.user.is_authenticated and request.user.username != '':
		return render(request, 'dashboard.html')

	user_form = UserForm()
	return render(request, 'public/home.html', {'user_form' : user_form})