# Generated by Django 3.2.6 on 2021-08-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, null=True)),
                ('trade_name', models.CharField(max_length=100, null=True)),
                ('high', models.FloatField(max_length=100, null=True)),
                ('low', models.FloatField(max_length=100, null=True)),
                ('open', models.FloatField(max_length=100, null=True)),
                ('close', models.FloatField(max_length=100, null=True)),
                ('volume', models.IntegerField(null=True)),
            ],
        ),
    ]
