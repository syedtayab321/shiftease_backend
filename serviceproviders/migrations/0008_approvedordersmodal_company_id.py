# Generated by Django 5.0.7 on 2024-10-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0007_approvedordersmodal_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvedordersmodal',
            name='Company_id',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
