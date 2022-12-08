# Generated by Django 4.1.2 on 2022-11-07 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_rename_category_id_productmodel_category_and_more'),
        ('buyer', '0002_alter_buyermodel_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shipping', models.CharField(max_length=500)),
                ('Phone', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Total_price', models.IntegerField()),
                ('Buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyermodel')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.productmodel')),
            ],
        ),
    ]
