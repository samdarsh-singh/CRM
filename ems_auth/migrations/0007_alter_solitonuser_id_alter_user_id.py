# Generated by Django 4.0.3 on 2022-06-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_auth', '0006_auto_20220503_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solitonuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
