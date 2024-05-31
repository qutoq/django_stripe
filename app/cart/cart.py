from decimal import Decimal
from django.conf import settings
from shop.models import Item


def display(price):
    return "{0:.2f}".format(price / 100)


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item, quantity=1, update_quantity=False):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'name': item.name, 'quantity': 0, 'price': str(item.price)}
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def remove_all(self):
        self.cart = self.session[settings.CART_SESSION_ID] = {}

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        for item in items:
            self.cart[str(item.id)]['item'] = item

        for items in self.cart.values():
            items['name'] = items['name']
            items['price'] = Decimal(items['price'])
            items['total_price'] = items['price'] * items['quantity']
            items['display_price'] = display(items['price'])
            items['display_total_price'] = display(items['total_price'])
            yield items

    def __len__(self):
        return sum(items['quantity'] for items in self.cart.values())

    def get_total_price(self):
        total = sum(Decimal(items['price']) * items['quantity'] for items in self.cart.values())
        return display(total)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
