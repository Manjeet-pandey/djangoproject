from django.db import models

# Create your models here.
class AddProduct(models.Model):
    productName= models.CharField(max_length=100)
    productMaterialItemCode= models.CharField(max_length=100)
    productBrandNewSellingRate= models.FloatField()
    productSecondHandSellingRate= models.FloatField()
    productLossRate=models.FloatField()
    productRepairRate=models.FloatField()
    productDailyRentalRate=models.FloatField()
    productWeekyRentalRate=models.FloatField()
    productMonthlyRentalRate=models.FloatField()
    productDailyHireCharge=models.FloatField()
    productWeekyHireCharge=models.FloatField()
    productMonthlyHireCharge=models.FloatField()
    productRecordedBy=models.CharField(max_length=100)
    supplierName=models.CharField(max_length=100)
    remarks=models.CharField(max_length=200)
    stock=models.IntegerField()

class AddProject(models.Model):
    projectTitle=models.CharField(max_length=100)
    projectId=models.IntegerField()
    projectContractNo=models.IntegerField()
    projectSiteLocation=models.CharField(max_length=100)
    projectMailLocation=models.CharField(max_length=100)
    orderNumber=models.IntegerField()
    projectStatus=models.CharField(max_length=100)
    projectRecordedBy=models.CharField(max_length=100)
    txTruckRates=models.IntegerField()
    remarks=models.CharField(max_length=100)

class AddSupplier(models.Model):
    supplierId=models.IntegerField()
    supplierName=models.CharField(max_length=100)
    supplierAddress=models.CharField(max_length=100)
    supplierUrl=models.URLField(max_length=2083)
    supplierContactPerson=models.CharField(max_length=100)
    supplierContact1=models.CharField(max_length=30)
    supplierContact2=models.CharField(max_length=30)
    supplierContactFax=models.CharField(max_length=100)
    supplierEmail=models.EmailField(max_length=100)
    

  