import stripe
from django_stripe.settings import STRIPE_SECRET_KEY, DOMAIN, SECRET_WEBHOOK
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import logging

from .task import send_email_task


stripe.api_key = STRIPE_SECRET_KEY

# payment

def new_stripe_session(line, discount, tax, order, page_url):
    if discount is not None:
        discount_id = discount.id
    else:
        discount_id = None
    add_coupon(discount)
    session = stripe.checkout.Session.create(
        line_items=line,
        discounts=[{'coupon': discount_id}],
        mode='payment',
        metadata={"order_id": order.id},
        success_url=DOMAIN + "/success/",
        cancel_url=DOMAIN + page_url,
    )
    return session


def add_coupon(discount):
    try:
        stripe.Coupon.create(duration="once", id=discount.id, percent_off=discount.percent_off, name=discount.name)
    except:
        pass


def add_tax(tax):
    if tax is not None and tax.stripe_id == '':
        tax_stripe = stripe.TaxRate.create(display_name=tax.name, percentage=tax.value, inclusive=True)
        tax.stripe_id = tax_stripe.id
        tax.save(update_fields=['stripe_id'])

# webhook
#logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger('myapp')

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, SECRET_WEBHOOK
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)


    if event['type'] == 'checkout.session.completed':
        session = event['data']['object'] 

        customer_email = session["customer_details"]["email"]
        customer_name = session["customer_details"]["name"]
        order_id = session["metadata"]["order_id"]

        from .models import Order # hoba

        order = Order.objects.get(id=order_id)
        order.paid = True
        order.save()
        send_email_task.delay(customer_email, order_id, customer_name)
    
    return HttpResponse(status=200)