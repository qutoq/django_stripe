from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>', views.cart_add, name='cart_add'),
    path('remove/', views.cart_remove_all, name='cart_remove_all'),
    path('remove/<int:item_id>)', views.cart_remove, name='cart_remove'),
]

app_name = 'cart'
