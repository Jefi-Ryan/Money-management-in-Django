# Generated by Django 3.2.4 on 2021-07-25 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_bills'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bills',
            new_name='bill',
        ),
    ]