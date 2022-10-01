from django import template
from django.template.defaultfilters import timeuntil_filter
from django.utils import translation

import re


register = template.Library()

@register.simple_tag
def active(request, pattern):
    print(request)
    print(pattern)
    if pattern == request.path:
    #if re.search(pattern, request.path):
        return 'active'
    return ''

@register.simple_tag
def active_search(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.filter
def timeuntil_it(value, arg=None):
    with translation.override('it'):
        time_until = timeuntil_filter(value, arg)
    return time_until

