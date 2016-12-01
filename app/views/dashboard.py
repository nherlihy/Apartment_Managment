import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from app.forms.expense import ExpenseForm
from app.models import Expense

def ajax_add_expense(request):
	if request.method == 'POST':
		response = {}
		data = {}
		expense_form = ExpenseForm(data=request.POST)

		if expense_form.is_valid():
			expense = expense_form.save(commit=False)
			expense.shared_by = request.user.member.group
			expense.split_cost = expense.total_cost / request.user.member.group.members.count()
			expense.save()

			data['expense'] = serializers.serialize("json", [expense,])
			data['pay_to'] = expense.pay_to.user.username
			data['request_user'] = request.user.username
			response['data'] = data
			response['success'] = 'success'

		else:
			errors = expense_form.errors.as_json()
			data['errors'] = errors
			response['data'] = data
			response['failed'] = 'failed'


		return HttpResponse(json.dumps(response), content_type='application/json')

def ajax_clear_expense(request):
	if request.method == 'PUT':
		response = {}
		data = {}
		expense_id = QueryDict(request.body).get('id')
		expense = Expense.objects.get(id=expense_id)
		expense.total_cost = 0.00
		expense.split_cost = 0.00
		expense.is_payed = True
		expense.save()

		data['expense'] = serializers.serialize("json", [expense,])
		data['pay_to'] = expense.pay_to.user.username
		response['data'] = data
		response['success'] = 'success'

	return HttpResponse(json.dumps(response), content_type='application/json')



