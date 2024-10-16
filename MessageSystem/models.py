from django.db import models

# Create your models here.
class AdminMessageModal(models.Model):
      sender_id=models.IntegerField()
      receiver_id=models.IntegerField()
      sender_name=models.CharField(max_length=100)
      receiver_name=models.CharField(max_length=100)
      content=models.CharField(max_length=1000)
      message_time=models.DateTimeField(auto_now_add=True)


class UserMessageModal(models.Model):
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    message_time = models.DateTimeField(auto_now_add=True)


class ProviderMessageModal(models.Model):
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    message_time = models.DateTimeField(auto_now_add=True)