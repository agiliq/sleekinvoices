from django.contrib import admin
from .models import company
from base.admin import admin_site

# Register your models here.

@admin.register(company, site=admin_site)
class CompanyAdmin(admin.ModelAdmin):
    model = company
    fieldsets = (
        (None, {'fields': ('company_name','country')}),
        ('Company Address', {'fields': ('street_address', 'city', 'state', 'zip_code')}),
        
    )
    list_display = ['company_name','created', 'modified']
    readonly_fields = ('created', 'modified')

