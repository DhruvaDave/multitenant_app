# Generated by Django 3.1.1 on 2020-09-09 14:19

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_auto_20200909_1417'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sales', '0002_auto_20200909_1417'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Salesperson',
        ),
        migrations.CreateModel(
            name='Salesperson',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
