from django.db import models

# 🏷️ التصنيفات (دفاتر – مكتب – تطوير الذات – رقمية)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")
    slug = models.SlugField(unique=True, verbose_name="رابط القسم")

    class Meta:
        verbose_name = "التصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


# 🛍️ المنتجات
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="القسم")

    class Meta:
        verbose_name = "المنتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
