from django.contrib import admin
from .models import Employee, Inventory, Projects, Customer, Category, Quotations, QuotationItems, Invoices, InvoiceItems, TimeSheet

# Register your models here.

admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Category)
admin.site.register(Projects)
admin.site.register(Customer)
admin.site.register(Quotations)
admin.site.register(InvoiceItems)
admin.site.register(TimeSheet)
admin.site.register(QuotationItems)
admin.site.register(Invoices)