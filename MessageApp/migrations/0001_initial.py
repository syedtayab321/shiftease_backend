# Generated by Django 5.0.7 on 2024-10-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMessageModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderId', models.IntegerField()),
                ('receiverId', models.IntegerField()),
                ('senderName', models.CharField(max_length=100)),
                ('receiverName', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('message_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderMessageModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderId', models.IntegerField()),
                ('receiverId', models.IntegerField()),
                ('senderName', models.CharField(max_length=100)),
                ('receiverName', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('message_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMessageModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderId', models.IntegerField()),
                ('receiverId', models.IntegerField()),
                ('senderName', models.CharField(max_length=100)),
                ('receiverName', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('message_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
