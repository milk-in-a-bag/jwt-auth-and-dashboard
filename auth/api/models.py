from django.db import models

# Create your models here.

class SystemSettings(models.Model):

    status_choices = [
        ("In stock", "In stock"),
        ("On backorder", "On backorder"),
        ("In transit", "In transit"),
        ("Allocated", "Allocated"),
        ("Shipped", "Shipped"),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    website = models.URLField()
    logo = models.ImageField()
    status = models.CharField(choices=status_choices)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    office_contact = models.CharField(max_length=10)
    personal_contact = models.CharField(max_length=10)

    def __str__(self):
        return self.employee_name

class Category(models.Model):

    status_choices = [
        ("In stock", "In stock"),
        ("On backorder", "On backorder"),
        ("In transit", "In transit"),
        ("Allocated", "Allocated"),
        ("Shipped", "Shipped"),
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(choices=status_choices)

    def __str__(self):
        return self.name

class Inventory(models.Model):

    status_choices = [
        ("In stock", "In stock"),
        ("On backorder", "On backorder"),
        ("In transit", "In transit"),
        ("Allocated", "Allocated"),
        ("Shipped", "Shipped"),
    ]

    item_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length = 100)
    description = models.TextField()
    date_of_manufacture = models.DateField()
    warrant = models.IntegerField()
    warrant_expiry = models.DateField()
    serial = models.CharField()
    status = models.TextField(choices=status_choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='inventory')
    landing_price = models.IntegerField()
    selling_price = models.IntegerField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    project_head = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projects')
    project_status = models.CharField(max_length=20)

    def __str__(self):
        return self.project_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    physical_address = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=10)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.customer_name
    
class Quotations(models.Model):
    title = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='quotations')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name= 'quotations')
    
    def __str__(self):
        return self.title
    
class QuotationItems(models.Model):
    quotation = models.ForeignKey(Quotations, on_delete=models.CASCADE, related_name='quotation_items')
    description = models.TextField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory')

    def __str__(self):
        return self.inventory
    
class Invoices(models.Model):
    title = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='invoices')

    def __str__(self):
        return self.title
    
class InvoiceItems(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE, related_name='invoice_items')
    description = models.TextField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='invoice_items')

    def __str__(self):
        return self.inventory
    
class TimeSheet(models.Model):
    activity = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='timesheet')
    start_date = models.DateField()
    end_date = models.DateField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='timesheet')
    status = models.TextField()

    def __str__(self):
        return self.activity