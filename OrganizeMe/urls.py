from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🏠 الصفحة الرئيسية
    path('', include('products.urls')),   # الصفحة الرئيسية وأقسام المنتجات

    # 🛍️ روابط صفحات المنتجات مع البادئة /products/
    path('products/', include('products.urls')),

    # 🔐 الحسابات
    path('accounts/', include('accounts.urls')),

    # 🧾 الطلبات
    path('orders/', include('orders.urls')),
]

# 📸 عرض ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
