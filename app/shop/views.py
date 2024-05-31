from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Item, OrderItem, Order
from cart.forms import CartAddItemForm, OrderForm
from cart.cart import Cart
from .stripy import new_stripe_session, add_tax
from django_stripe.settings import DOMAIN


def main(request):
    items = Item.objects.all()
    return render(request, 'shop/test.html', {'items': items})


def item_view(request, id):
    item = get_object_or_404(Item, id=id)
    cart_item_form = CartAddItemForm()
    return render(request, 'shop/item_view.html', {'item': item, 'cart_item_form': cart_item_form})


@require_POST
def new_order(request):
    cart = Cart(request)
    if len(cart) != 0:
        order = Order()
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order.tax = cd['tax']
            order.discount = cd['discount']
        order.save()
        flag = False
        if order.tax is not None:
            add_tax(order.tax)
            flag = True
        line = []
        for item in cart:
            op = {'price_data': {'currency': 'usd', 'product_data': {'name': item['name'], },
                                        'unit_amount': item['price']},
                         'quantity': item['quantity']}
            if flag:
                op['tax_rates'] = [order.tax.stripe_id]
            line.append(op)
            OrderItem.objects.create(order=order, item=item['item'], price=item['price'], quantity=item['quantity'])

        session = new_stripe_session(line, order.discount, order.tax, order, "/cart")

        return redirect(session.url, code=303)
    else:
        return redirect('shop:main')


def buy_item(request, id):
    item = Item.objects.filter(id=id).first()
    order = Order()
    order.save()
    OrderItem.objects.create(order=order, item=item, price=item.price, quantity=1)

    img_url = []
    try:
        if DOMAIN != "http://127.0.0.1:8000":
            img_url = [str(DOMAIN + '/static' + item.image.url)]
    except:
        pass

    line = [{'price_data': {'currency': 'usd', 'product_data': {'name': item.name, 'images': img_url},
                            'unit_amount': item.price, }, 'quantity': 1, }]
    session = new_stripe_session(line, None, None, order, "/item/" + str(id))

    return redirect(session.url, code=303)


def success(request):
    cart = Cart(request)
    cart.clear()
    return render(request, "shop/success.html")



