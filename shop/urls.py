from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('item/<int:id>/', views.item_view, name='item_view'),
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    path('create/', views.new_order, name='order_create'),
    path('success/', views.success, name='success'),
]

app_name = 'shop'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)