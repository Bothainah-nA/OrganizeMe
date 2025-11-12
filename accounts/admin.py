from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'country', 'joined_at')
    search_fields = ('user__username', 'phone', 'city', 'country')
    list_filter = ('city', 'country')
    readonly_fields = ('joined_at',)
    ordering = ('-joined_at',)
    list_display_links = ('user',)

    class Meta:
        verbose_name = "ملف المستخدم"
        verbose_name_plural = "ملفات المستخدمين"
