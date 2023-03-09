from django.contrib import admin
from core.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',
              'date_joined', 'last_login')
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')


admin.site.register(User, UserAdmin)
