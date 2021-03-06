# Generated by Django 2.2.11 on 2020-04-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScaffoldApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectTitle', models.CharField(max_length=100)),
                ('projectId', models.IntegerField()),
                ('projectContractNo', models.IntegerField()),
                ('projectSiteLocation', models.CharField(max_length=100)),
                ('projectMailLocation', models.CharField(max_length=100)),
                ('orderNumber', models.IntegerField()),
                ('projectStatus', models.CharField(max_length=100)),
                ('projectRecordedBy', models.CharField(max_length=100)),
                ('txTruckRates', models.IntegerField()),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]
