# Generated by Django 3.2.8 on 2021-11-02 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_rating_product'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
    ]
