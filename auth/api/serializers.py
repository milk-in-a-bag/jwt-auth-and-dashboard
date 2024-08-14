from rest_framework import serializers
from .models import SystemSettings, Employee, Inventory, Projects, Customer, Category, Quotations, QuotationItems, Invoices, InvoiceItems, TimeSheet

class SystemSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSettings
        fields = ('__all__')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('__all__')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('__all__')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class QuotationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotations
        fields = ('__all__')

class QuotationItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItems
        fields = ('__all__')

class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = ('__all__')

class InvoiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItems
        fields = ('__all__')

class TimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheet
        fields = ('__all__')