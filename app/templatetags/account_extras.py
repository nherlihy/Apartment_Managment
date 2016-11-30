from django import template
from django.template.defaultfilters import stringfilter
from random import randint

register = template.Library()

# This file allows for custom functions that can be embedded in html


@register.filter(name='initials')
@stringfilter
def initials(name):
    return name[0]

@register.filter(name='profile_image')
def profile_image(value):
    css_class = randint(1, 5)
    return {
        1: 'profile-1',
        2: 'profile-2',
        3: 'profile-3',
        4: 'profile-4',
        5: 'profile-5',
    }[css_class]
