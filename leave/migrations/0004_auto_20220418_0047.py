# Generated by Django 3.1.12 on 2022-04-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_alter_annual_planner_id_alter_leave_types_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual_planner',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leave_types',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leaveplan',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leaverecord',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]