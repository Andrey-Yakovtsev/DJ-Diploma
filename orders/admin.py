from django.contrib import admin
from .models import Order, OrderItem


class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'phone', 'email', 'address', 'city',
                    'created', 'updated', 'paid']
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemsInline]
