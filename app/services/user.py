from django.contrib.auth.models import User

from app.models import Member

def user_is_member(user):
	try:
		user.member
		return True

	except Member.DoesNotExist:
		return False