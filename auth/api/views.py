from rest_framework import viewsets
from .models import (
    SystemSettings, Employee, Inventory, Projects, Customer,
    Category, Quotations, QuotationItems, Invoices, InvoiceItems, TimeSheet
)
from .serializers import (
    SystemSettingsSerializer, EmployeeSerializer, InventorySerializer,
    ProjectSerializer, CustomerSerializer, CategorySerializer,
    QuotationsSerializer, QuotationItemsSerializer, InvoicesSerializer,
    InvoiceItemsSerializer, TimeSheetSerializer
)

# SystemSettings ViewSet
class SystemSettingsViewSet(viewsets.ModelViewSet):
    queryset = SystemSettings.objects.all()
    serializer_class = SystemSettingsSerializer

# Employee ViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Inventory ViewSet
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

# Customer ViewSet
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Quotation ViewSet
class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotations.objects.all()
    serializer_class = QuotationsSerializer

# QuotationItems ViewSet
class QuotationItemsViewSet(viewsets.ModelViewSet):
    queryset = QuotationItems.objects.all()
    serializer_class = QuotationItemsSerializer

# Invoices ViewSet
class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer

# InvoiceItems ViewSet
class InvoiceItemsViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer

# Timesheet ViewSet
class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer
