import json
import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import HttpResponseRedirect, HttpResponse, render

from app.forms.user_registration import UserForm
from app.forms.group import GroupForm
from app.forms.login import LoginForm
from app.models import *

@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')

def log_in(request):
	if request.method == 'POST':
		login_form = LoginForm(data=request.POST)
		if login_form.is_valid():
			response = {}
			data = {}
			user = authenticate(username=request.POST['login_username'], password=request.POST['login_password'])
			if user:
				if user.is_active:
					login(request, user)
					data['url'] = "http://%s%s" % (request.get_host(), '/')
					response['success'] = 'success'
					response['data'] = data
					return HttpResponse(json.dumps(response), content_type='application/json')
				else:
					# User is not active
					data['errors'] = ["Your Account is disabled"]
					response['data'] = data
					response['failed'] = 'failed'
					return HttpResponse(json.dumps(response), content_type='application/json')

			else:
				data['errors'] = ["Invalid login information"]
				response['data'] = data
				response['failed'] = 'failed'
				return HttpResponse(json.dumps(response), content_type='application/json')
	else:
		user_form = UserForm()
		login_form = LoginForm()
		return render(request, 'public/home.html', {'user_form' : user_form, 'login_form' : login_form})

@login_required
def register(request):
	group_form = GroupForm()
	return render(request, 'account/group.html', {'group_form' : group_form})

def create_group(request):
	if request.method == 'POST':
		response = {}
		data = {}

		group_form = GroupForm(data=request.POST)
		if len(request.POST['group_name']) > 30:
			data['errors'] = ["Group name must be less than 30 characters"]
			response['data'] = data
			response['failed'] = 'failed'
			return HttpResponse(json.dumps(response), content_type='application/json')

		if group_form.is_valid():
			group_code = uuid.uuid4().hex[:6].upper()
			group = Group.objects.create(name=request.POST['group_name'], code=group_code)
			member = Member.objects.create(user=request.user, group=group)

			data['url'] = "http://%s%s" % (request.get_host(), '/')
			response['success'] = 'success'
			response['data'] = data

		else:
			errors = group_form.errors.as_json()
			data['errors'] = errors
			response['data'] = data
			response['failed'] = 'failed'

		return HttpResponse(json.dumps(response), content_type='application/json')

def add_to_group(request):
	if request.method == 'POST':
		response = {}
		data = {}

		group_code = request.POST['group_code']
		try:
			group = Group.objects.get(code=group_code)
			member = Member.objects.create(user=request.user, group=group)
			data['url'] = "http://%s%s" % (request.get_host(), '/')
			response['success'] = 'success'
			response['data'] = data

		except Group.DoesNotExist:
			data['errors'] = ["There is no group that matchs that code"]
			response['data'] = data
			response['failed'] = 'failed'

		return HttpResponse(json.dumps(response), content_type='application/json')


