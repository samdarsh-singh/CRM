# Generated by Django 4.0.3 on 2022-04-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0002_bankdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetails',
            name='customer_name',
            field=models.CharField(max_length=50),
        ),
    ]
