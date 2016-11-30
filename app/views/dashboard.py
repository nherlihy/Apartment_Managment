from django.shortcuts import render
from app.forms.expense import ExpenseForm
from app.models.models import Expense


def dashboard(request):
    group_expenses = Expense.objects.order_by('id')
    expense_form = ExpenseForm()
    return render(request, 'dashboard/dashboard.html', {'expense_form': expense_form, 'group_expenses': group_expenses})
