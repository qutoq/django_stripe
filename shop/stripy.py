import stripe
from django_stripe.settings import STRIPE_SECRET_KEY, DOMAIN

stripe.api_key = STRIPE_SECRET_KEY


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
