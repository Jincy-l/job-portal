# Generated by Django 5.0.6 on 2024-07-01 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobport', '0022_employee_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='userid',
        ),
    ]
