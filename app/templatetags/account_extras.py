from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# This file allows for custom functions that can be embedded in html


@register.filter(name='initials')
@stringfilter
def initials(name):
    return name[0]

