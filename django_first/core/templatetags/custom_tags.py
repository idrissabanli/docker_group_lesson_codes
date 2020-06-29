from django.template import Library
from datetime import datetime

register = Library()

@register.simple_tag
def current_datetime():
    return datetime.today()