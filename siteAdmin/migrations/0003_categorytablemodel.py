# Generated by Django 4.1.2 on 2022-10-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteAdmin', '0002_rename_password_adminmodel_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoryTableModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=255)),
            ],
        ),
    ]