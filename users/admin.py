from django.contrib import admin
from .models import User
from base.admin import admin_site

# Register your models here.
@admin.register(User, site=admin_site)
class UserAdmin(admin.ModelAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'avatar', 'company')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_staff', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined', 'last_login')


   

