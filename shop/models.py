from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .stripy import add_coupon


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    image = models.ImageField(upload_to='items/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(max_length=1000, verbose_name='Описание', null=True)
    price = models.IntegerField(default=0, verbose_name='Цена')

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return str(self.name) + ' | ' + self.get_display_price()

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Discount(models.Model):
    name = models.CharField(max_length=30,unique=True,)
    percent_off = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])

    class Meta:
        verbose_name = 'купон'
        verbose_name_plural = 'купоны'

    def __str__(self):
        return str(self.name) + ' - ' + f'{self.percent_off}%'


class Tax(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    name = models.CharField(max_length=30, unique=True)
    stripe_id = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'налог'
        verbose_name_plural = 'налоги'

    def __str__(self):
        return str(self.name) + ' - ' + f'{self.value}%'


class Order(models.Model):
    created = models.DateTimeField(editable=True, auto_now_add=True)
    paid = models.BooleanField(default=False)
    tax = models.ForeignKey(Tax, null=True, default=None, on_delete=models.SET_DEFAULT)
    discount = models.ForeignKey(Discount, null=True, default=None, on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return 'Заказ {}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='order_items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'позиция товара'
        verbose_name_plural = 'позиции товаров'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
