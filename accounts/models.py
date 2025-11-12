from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="المستخدم")
    phone = models.CharField("رقم الجوال", max_length=15, blank=True, null=True)
    address = models.TextField("العنوان", blank=True, null=True)
    city = models.CharField("المدينة", max_length=100, blank=True, null=True)
    country = models.CharField("الدولة", max_length=100, blank=True, null=True)
    avatar = models.ImageField("الصورة الشخصية", upload_to='profiles/', blank=True, null=True)
    joined_at = models.DateTimeField("تاريخ الانضمام", auto_now_add=True)

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return self.user.username
