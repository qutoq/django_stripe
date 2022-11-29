from django import forms
from shop.models import Tax, Discount

ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddItemForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=ITEM_QUANTITY_CHOICES, coerce=int, label='')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.Form):
    discount = forms.ModelChoiceField(
        Discount.objects.all(),
        label='Купон:',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
        )
    tax = forms.ModelChoiceField(
        Tax.objects.all(),
        label='Налог:',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
        )
