from celery import shared_task
from time import sleep

@shared_task
def export_excel():
    print('ise dusdu')
    sleep(30)
    print('dayandi')
    return True