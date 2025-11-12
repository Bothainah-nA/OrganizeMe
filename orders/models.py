from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# الطلب
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد المعالجة'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"


# العناصر داخل الطلب
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
