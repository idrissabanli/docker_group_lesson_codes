from celery import shared_task
from time import sleep
from datetime import date, timedelta
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

from stories.models import Story, Recipe, Subscriber


@shared_task
def export_excel():
    print('ise dusdu')
    sleep(30)
    print('dayandi')
    return True


@shared_task
def send_email_to_subscribers():
    today  = date.today()
    yest = today - timedelta(days=1)
    recipes = Recipe.objects.filter(created_at__gte=yest, created_at__lt=today)
    stories = Story.objects.filter(created_at__gte=yest, created_at__lt=today)

    tempate_name = 'email-subscribers.html'
    context = {
        'recipes': recipes,
        'stories': stories,
        'site_address': settings.SITE_ADDRESS,
    }

    msg = render_to_string(tempate_name, context)
    subject  = 'New Stories'
    user_emails = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    # 'Select email from subscriber'
    message = EmailMessage(subject=subject, body=msg, from_email=settings.EMAIL_HOST_USER, to=user_emails)
    message.content_subtype = 'html'
    message.send()


