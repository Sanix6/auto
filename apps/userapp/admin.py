from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'phone']
    list_display_links = ['id', 'email', 'first_name', 'last_name', 'phone']
    ordering = ['-id']
    fieldsets = (
        ('Основаная информация', {'fields': ('email', 'password', 'first_name', 'last_name', 'phone')}),
        ('Права', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
        ('Активация', {'fields': ('is_active', 'code')})
    )
