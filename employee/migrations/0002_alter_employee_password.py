# Generated by Django 4.2 on 2024-09-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
