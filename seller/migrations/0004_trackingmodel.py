# Generated by Django 4.1.2 on 2022-11-08 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0008_ordermodel_phone'),
        ('seller', '0003_rename_category_id_productmodel_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=10)),
                ('Time', models.CharField(max_length=10)),
                ('Details', models.CharField(max_length=500)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.ordermodel')),
            ],
        ),
    ]
