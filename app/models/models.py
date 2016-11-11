from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.auth.models import User


# Each group should have a
class Group(models.Model):
    group_name = models.CharField(max_length=30)


# There can be any number of members in a group
class GroupMembers(models.Model):
    shared_group = models.ForeignKey(Group, related_name="shared_group")
    member = models.ForeignKey(User)


# Django generates an auto-incremented ID for users
class Expense(models.Model):
    cost = models.FloatField()
    pay_to = models.CharField(max_length=50)
    due_by = models.DateField()
    date_added = models.DateField("date_added", default=datetime.date.today)
    shared_by = models.ForeignKey(Group)


# Track what members are to share an expense
class SharedExpense(models.Model):
    group_name = models.ForeignKey(Group, related_name="group")
    member = models.ForeignKey(User, related_name="member")
    expense = models.ForeignKey(Expense, related_name="expense")
    is_paid = models.BooleanField()
