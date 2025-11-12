from pathlib import Path
import os

# =============================
# 📂 المسارات الأساسية
# =============================
BASE_DIR = Path(__file__).resolve().parent.parent

# المجلدات الرئيسية
TEMPLATES_DIR = BASE_DIR / 'templates'   # القوالب
STATIC_DIR = BASE_DIR / 'static'         # الملفات الثابتة (CSS, JS, Images)
MEDIA_DIR = BASE_DIR / 'media'           # الملفات المرفوعة (صور، ملفات المستخدمين)

# =============================
# 🔐 الإعدادات الأمنية
# =============================
SECRET_KEY = 'django-insecure-2_t0=dw+$+t*+_4b+4o=%7h&g5oids6&01(f==drw5)f=itdn%'
DEBUG = True
ALLOWED_HOSTS = []


# =============================
# 🧩 التطبيقات
# =============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'products.apps.ProductsConfig',
    'accounts.apps.AccountsConfig',
    'orders.apps.OrdersConfig',
]


# =============================
# ⚙️ الوسائط (Middleware)
# =============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =============================
# 🌐 المسارات العامة للمشروع
# =============================
ROOT_URLCONF = 'OrganizeMe.urls'


# =============================
# 🎨 إعدادات القوالب Templates
# =============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # تعريف مجلد القوالب الرئيسي
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =============================
# 🖥️ WSGI
# =============================
WSGI_APPLICATION = 'OrganizeMe.wsgi.application'


# =============================
# 🗄️ قاعدة البيانات
# =============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================
# 🔐 التحقق من كلمات المرور
# =============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =============================
# 🌍 اللغة والتوقيت
# =============================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# =============================
# 🧾 الملفات الثابتة (Static Files)
# =============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]       # مجلد static داخل المشروع
STATIC_ROOT = BASE_DIR / 'staticfiles'  # مجلد التجميع في حالة النشر


# =============================
# 🖼️ ملفات الوسائط (Media Files)
# =============================
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR                # مجلد تخزين الصور والملفات


# =============================
# ⚙️ الإعداد الافتراضي لمفاتيح الحقول
# =============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
