from django.contrib import admin
from .models import Item, Order, OrderItem, Tax, Discount


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['item']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'paid']
    list_filter = ['paid']
    inlines = [OrderItemInline]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tax)
admin.site.register(Discount)