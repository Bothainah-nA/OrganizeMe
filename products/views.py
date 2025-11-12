from django.shortcuts import render


# 🏠 الصفحة الرئيسية
def home(request):
    """
    الصفحة الرئيسية للمتجر — تحتوي على البنر الرئيسي وروابط الأقسام.
    """
    return render(request, 'home.html')


# 📘 دفاتر وأجندات
def notebooks(request):
    """
    صفحة قسم (دفاتر وأجندات):
    تعرض منتجات تساعد المستخدم على التخطيط والتنظيم اليومي.
    """
    return render(request, 'products-templates/notebooks.html')


# 💼 تنظيم المكتب
def office(request):
    """
    صفحة قسم (تنظيم المكتب):
    تحتوي على منتجات لتنظيم بيئة العمل وجعلها أكثر ترتيبًا وفعالية.
    """
    return render(request, 'products-templates/office.html')


# 🌿 تطوير الذات
def self_development(request):
    """
    صفحة قسم (تطوير الذات):
    تتضمن بطاقات وأدوات تحفيزية تساعد على النمو الشخصي.
    """
    return render(request, 'products-templates/self_development.html')


# 💻 المنتجات الرقمية
def digital(request):
    """
    صفحة قسم (المنتجات الرقمية):
    تحتوي على قوالب رقمية ومنتجات قابلة للطباعة تساعد في التنظيم الإلكتروني.
    """
    return render(request, 'products-templates/digital.html')
