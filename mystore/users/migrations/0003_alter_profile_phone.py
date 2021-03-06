# Generated by Django 3.2.8 on 2021-10-06 00:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator('\\d{3}?-?\\d{3}?-?\\d{4}', 'Only ten numbers and dashes allowed.')]),
        ),
    ]
