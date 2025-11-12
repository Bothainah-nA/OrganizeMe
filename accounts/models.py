from django.db import models
from django.contrib.auth.models import User

# الملف الشخصي لكل مستخدم
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="المدينة")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="الدولة")
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name="الصورة الشخصية")
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
