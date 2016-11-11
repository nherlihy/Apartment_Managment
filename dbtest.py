import django
from app.models import *

# justin = User.objects.create_user('justin', 'gagnej3@wit.edu', 'Wit123')
# nick = User.objects.create_user('nick', 'nick@wit.edu', 'Wit123')
# brandie = User.objects.create_user('brandie', 'brandie@wit.edu', 'Wit123')
# jones = User.objects.create_user('jones', 'jones@wit.edu', 'Wit123')
#
# group = Group.create('Web Apps')
#
# GroupMembers.create(group, justin)
# GroupMembers.create(group, nick)
# GroupMembers.create(group, brandie)

users = User.objects.all()
group = Group.objects.get(pk=1)

# for user in users:
#     member = Member.create(user, group)
#     member.save()

members = Member.objects.filter(group__pk=1)
memGroup = members[0].get_group()

# group = GroupMembers.get_members(users[0])
