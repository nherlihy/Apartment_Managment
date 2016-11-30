import django
from app.models import *
from app.models.models import Member

justin = User.objects.create_user('justin', 'justin@wit.edu', 'wit')
nick = User.objects.create_user('nick', 'nick@wit.edu', 'wit')
brandie = User.objects.create_user('brandie', 'brandie@wit.edu', 'wit')

group = Group.create('Web Apps', 'ABCDEF')

m1 = Member.create(justin, group)
m2 = Member.create(nick, group)
m3 = Member.create(brandie, group)

# I think we need to change an expense to reference members rather than users
Expense.create("Electric", 100.0, justin, group)
Expense.create("Internet", 60.0, nick, group)
Expense.create("Gas", 30.0, brandie, group)


# group_expenses = Expense.objects.all()
#
# # get will return an object
# member = Member.objects.get(user_id=1)
# group = Group.objects.get(id=member.group_id)
# members = Member.objects.filter(group_id=group)
# j = members[0]