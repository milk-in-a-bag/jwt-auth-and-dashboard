from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SystemSettingsViewSet, EmployeeViewSet, InventoryViewSet,
    ProjectViewSet, CustomerViewSet, CategoryViewSet, QuotationViewSet,
    QuotationItemsViewSet, InvoicesViewSet, InvoiceItemsViewSet, TimesheetViewSet
)

# Create a router and register all viewsets
router = DefaultRouter()
router.register(r'systemsettings', SystemSettingsViewSet, basename='systemsettings')
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'inventory', InventoryViewSet, basename='inventory')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'quotations', QuotationViewSet, basename='quotations')
router.register(r'quotationitems', QuotationItemsViewSet, basename='quotationitems')
router.register(r'invoices', InvoicesViewSet, basename='invoices')
router.register(r'invoiceitems', InvoiceItemsViewSet, basename='invoiceitems')
router.register(r'timesheets', TimesheetViewSet, basename='timesheets')

# Include the router-generated URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
