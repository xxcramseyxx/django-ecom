# Generated by Django 3.0.8 on 2020-10-18 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catagory',
            new_name='category',
        ),
    ]
