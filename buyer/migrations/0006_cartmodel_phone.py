# Generated by Django 4.1.2 on 2022-11-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='Phone',
            field=models.CharField(default='123', max_length=50),
        ),
    ]
