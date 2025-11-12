from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # التطبيق الرئيسي للمنتجات (الصفحة الرئيسية للموقع)
    path('', include('products.urls')),

    # حسابات المستخدمين
    path('accounts/', include('accounts.urls')),

    # الطلبات
    path('orders/', include('orders.urls')),
]
