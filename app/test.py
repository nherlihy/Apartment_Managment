from django.test import TestCase
from .models import *

class UserTestCase(TestCase):

    def getUsers(self):
        return User.objects.all()