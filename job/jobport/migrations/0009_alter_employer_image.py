# Generated by Django 5.0.6 on 2024-06-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobport', '0008_employer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='image',
            field=models.ImageField(upload_to='pic'),
        ),
    ]
