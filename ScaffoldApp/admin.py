from django.contrib import admin
from .models import *
# Register your models here.
class AppProductAdmin(admin.ModelAdmin):
    list_display=('productName','productMaterialItemCode','productRecordedBy','supplierName')

admin.site.register(AddProduct,AppProductAdmin)

class AddProjectAdmin(admin.ModelAdmin):
    list_display=('projectTitle','projectId','projectRecordedBy')
    
admin.site.register(AddProject,AddProjectAdmin)

class AddSupplierAdmin(admin.ModelAdmin):
    list_display=('supplierId','supplierName','supplierAddress')

admin.site.register(AddSupplier,AddSupplierAdmin)