from django.shortcuts import render
from rest_framework import generics

from .models import SystemSettings, Employee, Inventory, Projects, Customer, Category, Quotations, QuotationItems, Invoices, InvoiceItems, TimeSheet
from .serializers import SystemSettingsSerializer, EmployeeSerializer, InventorySerializer, ProjectSerializer, CustomerSerializer, CategorySerializer, QuotationsSerializer, QuotationItemsSerializer, InvoicesSerializer, InvoiceItemsSerializer, TimeSheetSerializer


# Create your views here.

class SystemSettingsList(generics.ListAPIView):
    serializer_class = SystemSettingsSerializer

    def get_queryset(self):
        queryset = SystemSettings.objects.all()        

        return queryset
    
class SystemSettingsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SystemSettingsSerializer
    queryset = SystemSettings.objects.all()        

class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()

        return queryset
    
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class InventoryList(generics.ListCreateAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.all()

        return queryset
    
class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Projects.objects.all()

        return queryset
    
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()

class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()

        return queryset
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()

        return queryset
    
class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()

        return queryset
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()

        return queryset
    
class QuotationsList(generics.ListCreateAPIView):
    serializer_class = QuotationsSerializer

    def get_queryset(self):
        queryset = Quotations.objects.all()

        return queryset
    
class QuotationsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuotationsSerializer

    def get_queryset(self):
        queryset = Quotations.objects.all()

        return queryset
    
class QuotationItemsList(generics.ListCreateAPIView):
    serializer_class = QuotationItemsSerializer

    def get_queryset(self):
        queryset = QuotationItems.objects.all()

        return queryset
    
class QuotationItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuotationItemsSerializer

    def get_queryset(self):
        queryset = QuotationItems.objects.all()

        return queryset
    
class InvoicesList(generics.ListCreateAPIView):
    serializer_class = InvoicesSerializer

    def get_queryset(self):
        queryset = Invoices.objects.all()

        return queryset
    
class InvoicesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoicesSerializer

    def get_queryset(self):
        queryset = Invoices.objects.all()

        return queryset
    
class InvoiceItemsList(generics.ListCreateAPIView):
    serializer_class = InvoiceItemsSerializer

    def get_queryset(self):
        queryset = InvoiceItems.objects.all()

        return queryset
    
class InvoiceItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceItemsSerializer

    def get_queryset(self):
        queryset = InvoiceItems.objects.all()

        return queryset
    
class TimeSheetList(generics.ListCreateAPIView):
    serializer_class = TimeSheetSerializer

    def get_queryset(self):
        queryset = TimeSheet.objects.all()

        return queryset
    
class TimeSheetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimeSheetSerializer

    def get_queryset(self):
        queryset = TimeSheet.objects.all()

        return queryset