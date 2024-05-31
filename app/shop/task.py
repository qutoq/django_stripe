from celery import shared_task
from django.core.mail import send_mail
from django_stripe.settings import EMAIL_HOST_USER


@shared_task
def send_email_task():
    return send_mail(
        "Subject here",
        "Here is the message.",
        EMAIL_HOST_USER,
        ["Den-73-73@yandex.ru"],
        fail_silently=False,
    )
