# Generated by Django 3.2.9 on 2022-04-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='tax_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='untaxed_amount',
            field=models.FloatField(),
        ),
    ]
