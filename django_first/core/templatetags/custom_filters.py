from django.template import Library

register = Library()

@register.filter
def split(value, split_by=' '):
    return value.split(split_by)

@register.filter
def first_char(value):
    return value[0]