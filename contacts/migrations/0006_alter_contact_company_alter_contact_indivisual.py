# Generated by Django 4.0.3 on 2022-04-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contact_company_n_alter_contact_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='indivisual',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]