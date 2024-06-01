from celery import shared_task
from django.core.mail import send_mail
from django_stripe.settings import EMAIL_HOST_USER


@shared_task
def send_email_task(mail, order, name):
    return send_mail(
        "Вы успешно оплатили заказ!",
        "Но, к сожалению, это тестовый магазин, на этом всё. Доставки не будет(" + '\n'
        "Номер заказа: " + order + ". Покупатель: " + name,
        EMAIL_HOST_USER,
        [mail],
        fail_silently=False,
    )
