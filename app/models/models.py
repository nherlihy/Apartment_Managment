from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.auth.models import User


# Each group should have a
class Group(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=6, unique=True, default="abcdef")

    @classmethod
    def create(cls, name, code):
        group = cls(name=name, code=code)
        group.save()
        return group

    def __str__(self):
        return "%s\tId: %s" % (self.name, self.code)

    class Meta:
        app_label = 'app'


class Member(models.Model):

    # Ensure each member and group combination is unique
    class Meta:
        unique_together = (('user', 'group'),)
        app_label = 'app'

    user = models.OneToOneField(User)
    group = models.ForeignKey(Group, related_name='members')

    def get_group(self):
        return Group.objects.get(pk=self.group_id)

    def get_group_info(self):
        return self.group.name

    @classmethod
    def create(cls, user, group):
        member = cls(user=user, group=group)
        member.save()
        return member

    def __str__(self):
        return "%s" % self.user


# Django generates an auto-incremented ID for users
class Expense(models.Model):
    description = models.CharField(default='Expense', max_length=40)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    split_cost = models.DecimalField(max_digits=10, decimal_places=2)
    pay_to = models.ForeignKey(Member)
    due_by = models.DateField(default=datetime.date.today)
    date_added = models.DateField("date_added", default=datetime.date.today)
    shared_by = models.ForeignKey(Group)
    is_payed = models.BooleanField(default=False)

    @classmethod
    def create(cls, description, cost, pay_to, shared_by):
        expense = cls(description=description, cost=cost, pay_to=pay_to, shared_by=shared_by)
        expense.save()
        return expense

    def __str__(self):
        return "Expense: %s\tCost: %s\tPay To: %s" % (self.description, self.cost, self.pay_to)

    class Meta:
        app_label = 'app'
