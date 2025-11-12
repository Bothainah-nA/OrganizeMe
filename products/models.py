from django.db import models

# التصنيفات العامة (دفاتر، أدوات، منتجات رقمية..)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم التصنيف")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")

    def __str__(self):
        return self.name


# المنتج
class Product(models.Model):
    PRODUCT_TYPES = [
        ('physical', 'ملموس'),
        ('digital', 'رقمي'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPES, default='physical', verbose_name="النوع")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة المنتج")
    digital_file = models.FileField(upload_to='digital_products/', blank=True, null=True, verbose_name="الملف الرقمي")
    stock = models.PositiveIntegerField(default=0, verbose_name="الكمية المتوفرة")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
