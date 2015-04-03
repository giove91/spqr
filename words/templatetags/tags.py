from django.template.base import Library
from django.template.defaultfilters import timeuntil_filter, date as date_filter
from django.utils import translation

import re


register = Library()

@register.simple_tag
def active(request, pattern):
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

