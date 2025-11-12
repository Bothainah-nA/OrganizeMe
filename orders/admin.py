from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')
    verbose_name = "عنصر في الطلب"
    verbose_name_plural = "عناصر الطلب"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    list_display_links = ('id',)

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('product__name',)
    ordering = ('order',)
    list_display_links = ('order',)

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلبات"
