# Generated by Django 5.0.7 on 2024-10-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0002_orderrequestsmodal'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrequestsmodal',
            name='package_price',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='addteammodel',
            name='company_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderrequestsmodal',
            name='Company_id',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orderrequestsmodal',
            name='package_id',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orderrequestsmodal',
            name='package_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='packagesmodel',
            name='company_id',
            field=models.IntegerField(),
        ),
    ]
