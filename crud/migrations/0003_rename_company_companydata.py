# Generated by Django 3.2.6 on 2021-08-10 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210810_1143'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='company',
            new_name='companyData',
        ),
    ]
