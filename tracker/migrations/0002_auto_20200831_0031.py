# Generated by Django 3.0.9 on 2020-08-30 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'permissions': [('change_expense_status', 'Can change the status of expense')]},
        ),
    ]