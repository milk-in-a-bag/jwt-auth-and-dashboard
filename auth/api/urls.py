from django.urls import path
from .views import SystemSettingsList, SystemSettingsDetail, EmployeeList, EmployeeDetail, InventoryList, InventoryDetail, ProjectList, ProjectDetail, CustomerList, CustomerDetail, CategoryList, CategoryDetail, QuotationsList, QuotationsDetail, QuotationItemsList, QuotationItemsDetail, InvoicesList, InvoicesDetail, InvoiceItemsList, InvoiceItemsDetail, TimeSheetList, TimeSheetDetail

urlpatterns = [
    path('systemsettings/', SystemSettingsList.as_view()),
     path('systemsettings/<int:pk>/', SystemSettingsDetail.as_view()),
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
    path('inventory/', InventoryList.as_view()),
    path('inventory/<int:pk>/', InventoryDetail.as_view()),
    path('project/', ProjectList.as_view()),
    path('project/<int:pk>/', ProjectDetail.as_view()),
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>/', CustomerDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('quotations/', QuotationsList.as_view()),
    path('quotations/<int:pk>/', QuotationsDetail.as_view()),
    path('quotationitems/', QuotationItemsList.as_view()),
    path('quotationitems/<int:pk>/', QuotationItemsDetail.as_view()),
    path('invoices/', InvoicesList.as_view()),
    path('invoices/<int:pk>/', InvoicesDetail.as_view()),
    path('invoiceitems/', InvoiceItemsList.as_view()),
    path('invoiceitems/<int:pk>/', InvoiceItemsDetail.as_view()),
    path('timesheet/', TimeSheetList.as_view()),
    path('timesheet/<int:pk>/', TimeSheetDetail.as_view()),
]