# Generated by Django 5.0.6 on 2024-06-26 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobport', '0017_alter_apply_jobid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='jobid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apply',
            name='userid',
            field=models.CharField(max_length=50),
        ),
    ]
