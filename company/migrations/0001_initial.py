# Generated by Django 3.1 on 2021-06-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=18)),
                ('trading_name', models.CharField(blank=True, max_length=200, null=True)),
                ('employeds', models.ManyToManyField(null=True, related_name='companies', to='user.Employee')),
            ],
        ),
    ]
