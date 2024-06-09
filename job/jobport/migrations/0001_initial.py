# Generated by Django 5.0.6 on 2024-06-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('addimfor', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
