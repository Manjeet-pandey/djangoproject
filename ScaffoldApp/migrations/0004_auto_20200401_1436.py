# Generated by Django 2.2.11 on 2020-04-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScaffoldApp', '0003_addsupplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addsupplier',
            name='supplierContact1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='addsupplier',
            name='supplierContact2',
            field=models.FloatField(),
        ),
    ]
