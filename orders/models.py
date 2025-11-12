from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد المعالجة'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="المستخدم")
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("آخر تحديث", auto_now=True)
    status = models.CharField("حالة الطلب", max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField("إجمالي السعر", max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField("الكمية", default=1)
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "عنصر في الطلب"
        verbose_name_plural = "عناصر الطلبات"

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
