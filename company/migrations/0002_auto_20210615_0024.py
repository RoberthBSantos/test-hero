# Generated by Django 3.1 on 2021-06-15 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='employeds',
            new_name='employees',
        ),
    ]
