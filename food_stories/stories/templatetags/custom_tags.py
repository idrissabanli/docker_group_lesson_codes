from django.template import Library
from stories.forms import SubscriberForm

register = Library()

@register.simple_tag
def get_subscriber_form():
    return SubscriberForm()