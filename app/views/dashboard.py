import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from app.forms.expense import ExpenseForm

def ajax_add_expense(request):
	if request.method == 'POST':
		response = {}
		data = {}
		expense_form = ExpenseForm(data=request.POST)

		if expense_form.is_valid():
			expense = expense_form.save(commit=False)
			expense.shared_by = request.user.member.group
			expense.save()

			data['expense'] = serializers.serialize("json", [expense,])
			response['data'] = data
			response['success'] = 'success'

		else:
			print "invalid"
			errors = expense_form.errors.as_json()
			data['errors'] = errors
			response['data'] = data
			response['failed'] = 'failed'
			print response


		return HttpResponse(json.dumps(response), content_type='application/json')