# Generated by Django 3.2.6 on 2021-08-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_auto_20210810_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='close',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='high',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='low',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='open',
            field=models.FloatField(max_length=100, null=True),
        ),
    ]
