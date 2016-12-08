from django.contrib import admin
from .models import invoice
from base.admin import admin_site

# Register your models here.

@admin.register(invoice, site=admin_site)
class InvoiceAdmin(admin.ModelAdmin):
	model = invoice



