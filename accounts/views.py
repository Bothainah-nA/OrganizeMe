from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# 🧍‍♀️ إنشاء حساب جديد
def register_view(request):
    """
    صفحة تسجيل مستخدم جديد
    """
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        # التحقق من الحقول المطلوبة
        if not username or not email or not password:
            messages.error(request, "الرجاء تعبئة جميع الحقول.")
            return redirect('register')

        # التحقق من تكرار اسم المستخدم
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم مسبقًا.")
            return redirect('register')

        # إنشاء المستخدم
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن ✨")
        return redirect('login')

    return render(request, 'accounts-templates/register.html')


# 🔐 تسجيل الدخول
def login_view(request):
    """
    صفحة تسجيل الدخول للمستخدمين
    """
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        if not username or not password:
            messages.error(request, "الرجاء إدخال اسم المستخدم وكلمة المرور.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"مرحبًا {user.username} 👋 تم تسجيل الدخول بنجاح!")
            return redirect('home')
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")

    return render(request, 'accounts-templates/login.html')


# 🚪 تسجيل الخروج
def logout_view(request):
    """
    تسجيل خروج المستخدم الحالي
    """
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح 👋")
    return redirect('home')
