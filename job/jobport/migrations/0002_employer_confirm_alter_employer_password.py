# Generated by Django 5.0.6 on 2024-06-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='confirm',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employer',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
