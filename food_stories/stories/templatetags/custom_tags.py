from django.template import Library
from stories.forms import SubscriberForm, Category

register = Library()

@register.simple_tag
def get_subscriber_form():
    return SubscriberForm()

@register.simple_tag
def get_categories():
    return Category.objects.all()[:3]

