# Generated by Django 5.0.6 on 2024-06-20 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobport', '0007_alter_postajob_jobdes'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
