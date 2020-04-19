from django import forms
from ScaffoldApp.models import *

class addProductForm(forms.ModelForm):
    productName=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name'}),
                                required=True,max_length=100)
    productMaterialItemCode=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Material Item Code'}),
                                required=True,max_length=100)
    productBrandNewSellingRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Brand-New Selling Rate'}),
                                required=True)
    productLossRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Loss Rate'}),
                                required=True)
    productRepairRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Repair Rate'}),
                                required=True)
    productDailyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Daily Rental Rate'}),
                                required=True)
    productWeekyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Weekly Rental Rate'}),
                                required=True)
    productMonthlyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Monthly Rental Rate'}),
                                required=True)
    productDailyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Daily Hire Charge'}),
                                required=True)
    productWeekyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Weekly Hire Charge'}),
                                required=True)
    productMonthlyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Monthly Hire Charge'}),
                                required=True)
    productRecordedBy=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Recorded By'}),
                                required=True,max_length=100)
    supplierName=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Supplier Name'}),
                                required=True,max_length=100)
    remarks=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Remarks'}),
                                required=True,max_length=200)
    class Meta:
        model=AddProduct
        fields=[
                'productName',
                'productMaterialItemCode',
                'productBrandNewSellingRate',
                'productLossRate',
                'productRepairRate',
                'productDailyRentalRate',
                'productWeekyRentalRate',
                'productMonthlyRentalRate',
                'productDailyHireCharge',
                'productWeekyHireCharge',
                'productMonthlyHireCharge',
                'productRecordedBy',
                'supplierName',
                'remarks'
               ]

class addProjectForm(forms.ModelForm):
    projectTitle=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Title'}),
                                 required=True,max_length=100)
    projectId=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Project ID'}),
                                 required=True)
    projectContractNo=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Project Contract No'}),
                                 required=True)
    projectSiteLocation=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Site Location'}),
                                 required=True,max_length=100)
    projectMailLocation=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Mail Location'}),
                                 required=True,max_length=100)
    orderNumber=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Order Number'}),
                                 required=True)
    projectStatus=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Status'}),
                                 required=True,max_length=100)
    projectRecordedBy=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Recorded By'}),
                                 required=True,max_length=100)
    txTruckRates=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Tx Truck Rates'}),
                                 required=True)
    remarks=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Remarks'}),
                                 required=True,max_length=200)
    class Meta:
        model=AddProject
        fields=[
                'projectTitle',
                'projectId',
                'projectContractNo',
                'projectSiteLocation',
                'projectMailLocation',
                'orderNumber',
                'projectStatus',
                'projectRecordedBy',
                'txTruckRates',
                'remarks'
               ]

class addSupplierForm(forms.ModelForm):
    supplierId=forms.IntegerField(widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Supplier ID'}),
                                   required=True)
    supplierName=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Name'}),
                                  required=True,max_length=100)
    supplierAddress=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Address'}),
                                  required=True,max_length=100)
    supplierUrl=forms.URLField(widget=forms.URLInput(
        attrs={'class':'form-control','placeholder':'Supplier URL'}),
                                  required=True,max_length=2083)
    supplierContactPerson=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact Person'}),
                                  required=True,max_length=100)
    supplierContact1=forms.CharField(widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact'}),
                                   required=True,max_length=30)
    supplierContact2=forms.CharField(widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact'}),
                                   required=True,max_length=30)
    supplierContactFax=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact Fax'}),
                                  required=True,max_length=100)
    supplierEmail=forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Email'}),
                                   required=True,max_length=100)
    class Meta:
        model=AddSupplier
        fields=[
                'supplierId',
                'supplierName',
                'supplierAddress',
                'supplierUrl',
                'supplierContactPerson',
                'supplierContact1',
                'supplierContact2',
                'supplierContactFax',
                'supplierEmail'
              ]
     