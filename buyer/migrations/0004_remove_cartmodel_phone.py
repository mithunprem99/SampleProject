# Generated by Django 4.1.2 on 2022-11-07 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_cartmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='Phone',
        ),
    ]
