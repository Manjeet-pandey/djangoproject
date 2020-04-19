# Generated by Django 2.2.11 on 2020-04-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScaffoldApp', '0002_addproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierId', models.IntegerField()),
                ('supplierName', models.CharField(max_length=100)),
                ('supplierAddress', models.CharField(max_length=100)),
                ('supplierUrl', models.URLField(max_length=2083)),
                ('supplierContactPerson', models.CharField(max_length=100)),
                ('supplierContact1', models.IntegerField()),
                ('supplierContact2', models.IntegerField()),
                ('supplierContactFax', models.CharField(max_length=100)),
                ('supplierEmail', models.EmailField(max_length=100)),
            ],
        ),
    ]
