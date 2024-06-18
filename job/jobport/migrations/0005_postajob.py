# Generated by Django 5.0.6 on 2024-06-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobport', '0004_employee_pin_employee_code_employee_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='postajob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(max_length=50)),
                ('jobdes', models.CharField(max_length=200)),
                ('jobtype', models.CharField(max_length=20)),
                ('quali', models.CharField(max_length=50)),
                ('schedule', models.CharField(max_length=20)),
                ('numberof', models.IntegerField()),
                ('image', models.ImageField(upload_to='pj')),
            ],
        ),
    ]
