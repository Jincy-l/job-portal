# Generated by Django 5.0.6 on 2024-06-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobport', '0011_postajob_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='postajob',
            name='pay',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]