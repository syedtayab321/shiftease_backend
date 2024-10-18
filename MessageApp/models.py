from django.db import models


class AdminMessageModal(models.Model):
    senderId = models.IntegerField()
    receiverId = models.IntegerField()
    senderName = models.CharField(max_length=100)
    receiverName = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    message_time = models.DateTimeField(auto_now_add=True)


class UserMessageModal(models.Model):
    senderId = models.IntegerField()
    receiverId = models.IntegerField()
    senderName = models.CharField(max_length=100)
    receiverName = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    message_time = models.DateTimeField(auto_now_add=True)


class ProviderMessageModal(models.Model):
    senderId = models.IntegerField()
    receiverId = models.IntegerField()
    senderName = models.CharField(max_length=100)
    receiverName = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    message_time = models.DateTimeField(auto_now_add=True)
